from django.db import models
from shipments_app.models import Shipment

class TransportTask(models.Model):

    TASK_TYPES = [
        ('port_pickup', 'استلام من الميناء'),
        ('port_delivery', 'نقل من الميناء'),
        ('warehouse', 'نقل إلى المستودع'),
        ('customer_delivery', 'تسليم للعميل'),
    ]

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, verbose_name="الشحنة المرتبطة")
    task_type = models.CharField(max_length=30, choices=TASK_TYPES, verbose_name="نوع المهمة")
    driver_name = models.CharField(max_length=100, verbose_name="اسم السائق")
    task_date = models.DateField(verbose_name="تاريخ المهمة")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    
    status = models.CharField(
        max_length=20,
        default="pending",
        verbose_name="الحالة",
        choices=[
            ("pending", "قيد التنفيذ"),
            ("done", "منفذة"),
            ("canceled", "ملغاة"),
        ]
    )

    class Meta:
        verbose_name = "مهمة نقل"
        verbose_name_plural = "مهام النقل"

    def __str__(self):
        return f"{self.shipment.container_number} - {self.task_type}"
