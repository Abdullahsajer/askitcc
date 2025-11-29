from django.db import models
from django.contrib.auth.models import User


# ===============================
# 1) جدول الأدوار Role
# ===============================
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم الدور")

    def __str__(self):
        return self.name


# ===============================
# 2) جدول مجموعات الصلاحيات PermissionGroup
# ===============================
class PermissionGroup(models.Model):
    code = models.CharField(max_length=100, unique=True)  # customers / shipments ...
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    def __str__(self):
        return self.name


# ===============================
# 3) جدول الصلاحيات Permission
# ===============================
class Permission(models.Model):
    group = models.ForeignKey(PermissionGroup, on_delete=models.CASCADE)
    code = models.CharField(max_length=150, unique=True)   # customers.add_customer
    name = models.CharField(max_length=200, verbose_name="اسم الصلاحية")

    def __str__(self):
        return f"{self.code}"


# ===============================
# 4) ربط الدور Role بالصلاحيات Permission
# ===============================
class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')

    def __str__(self):
        return f"{self.role} -> {self.permission.code}"


# ===============================
# 5) ملف المستخدم Profile
# ===============================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # صلاحيات إضافية محددة يدويًا
    custom_permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.user.username

    # إرجاع جميع الصلاحيات الفعلية (الدور + المخصصة)
    def get_all_permissions(self):
        role_perms = Permission.objects.filter(rolepermission__role=self.role)
        custom = self.custom_permissions.all()
        return set(list(role_perms) + list(custom))

    # التحقق من صلاحية محددة
    def has_permission(self, perm_code):
        return perm_code in [p.code for p in self.get_all_permissions()]
