from django.core.management.base import BaseCommand
from accounts_app.models import Role, PermissionGroup, Permission, RolePermission


class Command(BaseCommand):
    help = "إضافة الصلاحيات الافتراضية للنظام"

    def handle(self, *args, **kwargs):

        permissions_structure = {
            "customers": {
                "name": "العملاء",
                "perms": {
                    "view": "عرض العملاء",
                    "add": "إضافة عميل",
                    "edit": "تعديل عميل",
                    "delete": "حذف عميل",
                    "print": "طباعة بيانات العملاء",
                }
            },

            "shipments": {
                "name": "الشحنات",
                "perms": {
                    "view": "عرض الشحنات",
                    "add": "إضافة شحنة",
                    "edit": "تعديل شحنة",
                    "delete": "حذف شحنة",
                    "print": "طباعة بيانات الشحنات",
                }
            },

            "transport": {
                "name": "النقل",
                "perms": {
                    "view": "عرض مهام النقل",
                    "add": "إضافة مهمة نقل",
                    "edit": "تعديل مهمة نقل",
                    "delete": "حذف مهمة نقل",
                    "print": "طباعة مهام النقل",
                }
            },

            "workflow": {
                "name": "العمليات",
                "perms": {
                    "view": "عرض العمليات",
                    "add": "إضافة عملية",
                    "edit": "تعديل عملية",
                    "delete": "حذف عملية",
                    "print": "طباعة العمليات",
                }
            },

            "settings": {
                "name": "الإعدادات",
                "perms": {
                    "view": "عرض الإعدادات",
                    "edit": "تعديل الإعدادات",
                }
            },

            "users": {
                "name": "المستخدمين",
                "perms": {
                    "view": "عرض المستخدمين",
                    "add": "إضافة مستخدم",
                    "edit": "تعديل مستخدم",
                    "delete": "حذف مستخدم",
                }
            },
        }

        # إنشاء الدور "مدير النظام"
        admin_role, _ = Role.objects.get_or_create(name="مدير النظام")

        for group_code, group_data in permissions_structure.items():

            pg, _ = PermissionGroup.objects.get_or_create(
                code=group_code,
                name=group_data["name"]
            )

            for action, perm_name in group_data["perms"].items():

                full_code = f"{group_code}.{action}"

                p, _ = Permission.objects.get_or_create(
                    group=pg,
                    code=full_code,
                    name=perm_name
                )

                RolePermission.objects.get_or_create(role=admin_role, permission=p)

        self.stdout.write(self.style.SUCCESS("✨ تمت إضافة الصلاحيات الافتراضية بنجاح!"))
