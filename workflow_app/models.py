from django.db import models
from shipments_app.models import Shipment

class Workflow(models.Model):

    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE, verbose_name="الشحنة")

    CURRENT_STATUS = [
        ("arrived", "وصلت للميناء"),
        ("documents", "رفع المستندات"),
        ("customs", "جاري التخليص"),
        ("ready", "جاهزة للسحب"),
        ("delivered", "تم التسليم"),
    ]

    current_status = models.CharField(max_length=20, choices=CURRENT_STATUS, verbose_name="الحالة الحالية")

    last_update = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")

    class Meta:
        verbose_name = "عملية تخليص"
        verbose_name_plural = "عمليات التخليص"

    def __str__(self):
        return f"Workflow for {self.shipment.container_number}"


class WorkflowStep(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name="steps", verbose_name="العملية")
    step_name = models.CharField(max_length=200, verbose_name="اسم المرحلة")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="وقت العملية")

    class Meta:
        verbose_name = "مرحلة"
        verbose_name_plural = "مراحل التخليص"

    def __str__(self):
        return f"{self.step_name} - {self.workflow.shipment.container_number}"
