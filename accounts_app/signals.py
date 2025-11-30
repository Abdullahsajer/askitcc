from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts_app.models import Role, Permission, RolePermission


@receiver(post_save, sender=Permission)
def assign_permission_to_admin(sender, instance, created, **kwargs):
    """
    عند إنشاء أي صلاحية جديدة → تربط تلقائياً مع دور مدير النظام.
    """
    if created:
        try:
            admin_role = Role.objects.get(name="مدير النظام")
            RolePermission.objects.get_or_create(role=admin_role, permission=instance)
            print(f"✔ تمت إضافة الصلاحية الجديدة ({instance.code}) لدور مدير النظام.")
        except Role.DoesNotExist:
            print("⚠ لا يوجد دور باسم 'مدير النظام'.")
