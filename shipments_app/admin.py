from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):

    list_display = ("mbl_number", "container_number", "shipment_type",
                    "port", "arrival_date", "customer")
    list_filter = ("shipment_type", "port", "arrival_date")
    search_fields = ("mbl_number", "container_number")
    
    fieldsets = (
        ("بيانات الشحنة", {
            "fields": ("customer", "mbl_number", "container_number", "shipment_type")
        }),
        ("بيانات الوصول", {
            "fields": ("port", "arrival_date")
        }),
        ("ملاحظات", {
            "fields": ("notes",)
        }),
    )
