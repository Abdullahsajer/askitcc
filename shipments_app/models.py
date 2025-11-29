from django.db import models
from customers_app.models import Customer

class Shipment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="العميل")
    mbl_number = models.CharField(max_length=100, verbose_name="رقم البوليصة")
    container_number = models.CharField(max_length=50, verbose_name="رقم الحاوية")
    
    SHIPMENT_TYPES = [
        ('general', 'عامة'),
        ('food', 'مواد غذائية'),
        ('chemicals', 'كيماويات'),
        ('electronics', 'الكترونيات'),
    ]
    shipment_type = models.CharField(max_length=20, choices=SHIPMENT_TYPES, verbose_name="نوع الشحنة")

    port = models.CharField(max_length=100, verbose_name="ميناء الوصول")
    arrival_date = models.DateField(verbose_name="تاريخ الوصول")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    class Meta:
        verbose_name = "شحنة"
        verbose_name_plural = "الشحنات"

    def __str__(self):
        return f"{self.mbl_number} - {self.container_number}"
