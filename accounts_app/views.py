from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts_app.decorators import permission_required
from accounts_app.models import Profile, Role, PermissionGroup, Permission, RolePermission


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

            # إذا المستخدم لم يحدد له دور بعد
            if not profile.role:
                return redirect("/")

            role_name = profile.role.name

            redirect_map = {
                "مدير النظام": "/",
                "موظف تخليص": "/shipments/",
                "موظف نقل": "/transport/",
                "مشاهد فقط": "/",
            }

            return redirect(redirect_map.get(role_name, "/"))

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
# إضافة مستخدم جديد
# ====================================================
@login_required
@permission_required("users.add_user")
def add_user_view(request):

    roles = Role.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role_id = request.POST.get("role")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("accounts_app:add_user")

        user = User.objects.create_user(username=username, email=email, password=password)

        role = Role.objects.get(id=role_id)
        Profile.objects.create(user=user, role=role)

        messages.success(request, "تم إنشاء المستخدم بنجاح!")
        return redirect("accounts_app:users")

    return render(request, "accounts/add_user.html", {"roles": roles})


# ====================================================
# قائمة المستخدمين
# ====================================================
@login_required
@permission_required("users.view_user")
def users_list_view(request):
    users = User.objects.select_related("profile").all()
    return render(request, "accounts/users_list.html", {"users": users})


# ====================================================
# تعديل مستخدم
# ====================================================
@login_required
@permission_required("users.edit_user")
def edit_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    roles = Role.objects.all()

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")

        role_id = request.POST.get("role")
        profile.role = Role.objects.get(id=role_id)

        user.save()
        profile.save()

        messages.success(request, "تم تحديث بيانات المستخدم بنجاح!")
        return redirect("accounts_app:users")

    return render(request, "accounts/edit_user.html", {
        "user": user,
        "profile": profile,
        "roles": roles
    })


# ====================================================
# حذف مستخدم
# ====================================================
@login_required
@permission_required("users.delete_user")
def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "تم حذف المستخدم.")
    return redirect("accounts_app:users")


# ====================================================
# تعطيل مستخدم
# ====================================================
@login_required
@permission_required("users.edit_user")
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
@permission_required("users.edit_user")
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
@permission_required("users.edit_user")
def reset_password_view(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        user.set_password(new_password)
        user.save()

        messages.success(request, "تم تحديث كلمة المرور.")
        return redirect("accounts_app:edit_user", user_id=user_id)

    return render(request, "accounts/reset_password.html", {"user": user})


# ====================================================
# إدارة الصلاحيات
# ====================================================
@login_required
@permission_required("settings.edit_settings")
def permissions_view(request):

    roles = Role.objects.all()
    groups = PermissionGroup.objects.all()

    selected_role_id = request.GET.get("role")
    selected_role = None
    role_permissions = []

    if selected_role_id:
        selected_role = Role.objects.get(id=selected_role_id)
        role_permissions = RolePermission.objects.filter(role=selected_role).values_list("permission_id", flat=True)

    if request.method == "POST":
        selected_role_id = request.POST.get("role_id")
        selected_role = Role.objects.get(id=selected_role_id)

        # حذف القديمة
        RolePermission.objects.filter(role=selected_role).delete()

        # إضافة الجديدة
        new_perms = request.POST.getlist("permissions")
        for perm_id in new_perms:
            RolePermission.objects.create(
                role=selected_role,
                permission=Permission.objects.get(id=perm_id)
            )

        messages.success(request, "تم تحديث صلاحيات الدور بنجاح ✔")
        return redirect(f"/accounts/permissions/?role={selected_role.id}")

    return render(request, "accounts/permissions.html", {
        "roles": roles,
        "groups": groups,
        "selected_role": selected_role,
        "role_permissions": role_permissions,
    })
