from django import template
from accounts_app.models import RolePermission, Permission

register = template.Library()

@register.filter
def has_perm(user, perm_code):
    """يتحقق هل للمستخدم صلاحية معينة"""
    if not user.is_authenticated:
        return False

    profile = getattr(user, "profile", None)
    if not profile or not profile.role:
        return False

    try:
        perm = Permission.objects.get(code=perm_code)
    except Permission.DoesNotExist:
        return False

    return RolePermission.objects.filter(
        role=profile.role,
        permission=perm
    ).exists()
