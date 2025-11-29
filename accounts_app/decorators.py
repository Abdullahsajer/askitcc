from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("/accounts/login/")

            user_role = request.user.profile.role

            if user_role not in allowed_roles:
                messages.error(request, "ليس لديك صلاحية لدخول هذه الصفحة.")
                return redirect("/")

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
