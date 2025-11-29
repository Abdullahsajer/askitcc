from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# إضافة البروفايل داخل صفحة المستخدم
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "البيانات الإضافية"

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
