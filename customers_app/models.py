from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم العميل")
    cr_number = models.CharField(max_length=50, verbose_name="رقم السجل التجاري")
    cr_expiry_date = models.DateField(verbose_name="تاريخ انتهاء السجل")
    authorization_number = models.CharField(max_length=50, verbose_name="رقم التفويض")
    authorization_expiry = models.DateField(verbose_name="تاريخ انتهاء التفويض")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"

    def __str__(self):
        return self.name
