from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ("name", "cr_number", "cr_expiry_date",
                    "authorization_number", "authorization_expiry", "phone")
    search_fields = ("name", "cr_number", "authorization_number")
    list_filter = ("cr_expiry_date", "authorization_expiry")
    
    fieldsets = (
        ("بيانات العميل", {
            "fields": ("name", "phone", "email")
        }),
        ("السجل التجاري", {
            "fields": ("cr_number", "cr_expiry_date")
        }),
        ("التفويض", {
            "fields": ("authorization_number", "authorization_expiry")
        }),
        ("ملاحظات إضافية", {
            "fields": ("notes",)
        }),
    )
