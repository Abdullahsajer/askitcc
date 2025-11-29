from django.contrib import admin
from .models import CompanySettings

@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):

    list_display = ("company_name", "cr_number", "vat_number", "phone")
    search_fields = ("company_name", "cr_number", "vat_number")
    
    fieldsets = (
        ("المعلومات الأساسية", {
            "fields": ("company_name", "cr_number", "cr_expiry_days")
        }),
        ("تفاصيل التواصل", {
            "fields": ("phone", "email")
        }),
        ("الضريبة", {
            "fields": ("vat_number",)
        }),
        ("الحساب البنكي", {
            "fields": ("bank_name", "iban")
        }),
    )
