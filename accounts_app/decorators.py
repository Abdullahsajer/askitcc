from django.shortcuts import redirect, render
from accounts_app.models import Permission


def permission_required(perm_code):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            # غير مسجّل دخول
            if not request.user.is_authenticated:
                return redirect("accounts_app:login")

            profile = getattr(request.user, "profile", None)

            # لو ما عنده ملف أو دور
            if not profile or not profile.role:
                return render(request, "403.html", status=403)

            # تحميل جميع الصلاحيات (دور + مخصصة)
            user_permissions = [p.code for p in profile.get_all_permissions()]

            # التحقق هل يملك الصلاحية المطلوبة
            if perm_code not in user_permissions:
                return render(request, "403.html", status=403)

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator
