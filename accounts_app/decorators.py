from django.shortcuts import redirect
from django.contrib import messages
from accounts_app.models import Permission

def permission_required(permission_code):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("/accounts/login/")

            profile = request.user.profile

            # صلاحيات الدور Role
            role_permissions = set(
                profile.role.rolepermission_set.values_list("permission__code", flat=True)
            ) if profile.role else set()

            # صلاحيات مخصصة للمستخدم (Extra)
            custom_permissions = set(
                profile.custom_permissions.values_list("code", flat=True)
            )

            all_permissions = role_permissions.union(custom_permissions)

            if permission_code not in all_permissions:
                messages.error(request, "ليس لديك صلاحية لدخول هذه الصفحة.")
                return redirect("/")

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator
