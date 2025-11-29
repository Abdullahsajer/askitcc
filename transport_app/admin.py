from django.contrib import admin
from .models import TransportTask

@admin.register(TransportTask)
class TransportTaskAdmin(admin.ModelAdmin):

    list_display = ("shipment", "task_type", "driver_name", "task_date", "status")
    list_filter = ("task_type", "status", "task_date")
    search_fields = ("shipment__container_number", "driver_name")
    
    fieldsets = (
        ("بيانات المهمة", {
            "fields": ("shipment", "task_type", "driver_name", "task_date")
        }),
        ("الحالة", {
            "fields": ("status",)
        }),
        ("ملاحظات", {
            "fields": ("notes",)
        }),
    )
