from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts_app.decorators import role_required
from .models import Profile


# ====================================================
# تسجيل الدخول
# ====================================================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            profile, created = Profile.objects.get_or_create(user=user)

            redirect_map = {
                "admin": "/",
                "clearance": "/shipments/",
                "transport": "/transport/",
                "viewer": "/",
            }
            return redirect(redirect_map.get(profile.role, "/"))

        messages.error(request, "بيانات الدخول غير صحيحة!")
        return redirect("accounts_app:login")

    return render(request, "accounts/login.html")



# ====================================================
# تسجيل الخروج
# ====================================================
def logout_view(request):
    logout(request)
    return redirect("accounts_app:login")



# ====================================================
# إضافة مستخدم جديد (مدير النظام فقط)
# ====================================================
@login_required
@role_required(["admin"])
def add_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("accounts_app:add_user")

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, role=role)

        messages.success(request, "تم إنشاء المستخدم بنجاح!")
        return redirect("accounts_app:users")

    return render(request, "accounts/add_user.html")



# ====================================================
# قائمة المستخدمين
# ====================================================
@login_required
@role_required(["admin"])
def users_list_view(request):
    users = User.objects.all().order_by("username")
    return render(request, "accounts/users_list.html", {"users": users})



# ====================================================
# تعديل مستخدم
# ====================================================
@login_required
@role_required(["admin"])
def edit_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        profile.role = request.POST.get("role")

        user.save()
        profile.save()

        messages.success(request, "تم تحديث بيانات المستخدم بنجاح!")
        return redirect("accounts_app:users")

    return render(request, "accounts/edit_user.html", {
        "user": user,
        "profile": profile
    })



# ====================================================
# حذف مستخدم
# ====================================================
@login_required
@role_required(["admin"])
def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "تم حذف المستخدم.")
    return redirect("accounts_app:users")



# ====================================================
# تعطيل مستخدم
# ====================================================
@login_required
@role_required(["admin"])
def deactivate_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "تم تعطيل المستخدم.")
    return redirect("accounts_app:users")



# ====================================================
# تفعيل مستخدم
# ====================================================
@login_required
@role_required(["admin"])
def activate_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "تم تفعيل المستخدم.")
    return redirect("accounts_app:users")



# ====================================================
# إعادة تعيين كلمة المرور
# ====================================================
@login_required
@role_required(["admin"])
def reset_password_view(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        user.set_password(new_password)
        user.save()

        messages.success(request, "تم تحديث كلمة المرور.")
        return redirect("accounts_app:edit_user", user_id=user_id)

    return render(request, "accounts/reset_password.html", {"user": user})
