from django.db import models


class CompanySettings(models.Model):
    company_name = models.CharField(max_length=200, verbose_name="اسم الشركة")
    cr_number = models.CharField(max_length=50, verbose_name="رقم السجل التجاري")
    vat_number = models.CharField(max_length=50, verbose_name="الرقم الضريبي")
    phone = models.CharField(max_length=50, verbose_name="رقم التواصل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    iban = models.CharField(max_length=50, verbose_name="رقم الحساب البنكي (IBAN)")
    address = models.CharField(max_length=300, verbose_name="العنوان")

    class Meta:
        verbose_name = "إعدادات الشركة"
        verbose_name_plural = "إعدادات الشركة"

    def __str__(self):
        return self.company_name



class AlertsSettings(models.Model):
    notify_cr_expiry = models.BooleanField(default=True, verbose_name="تنبيه انتهاء السجل التجاري")
    notify_auth_expiry = models.BooleanField(default=True, verbose_name="تنبيه انتهاء التفويض")
    notify_missing_docs = models.BooleanField(default=True, verbose_name="تنبيه المستندات الناقصة")

    class Meta:
        verbose_name = "إعدادات التنبيهات"
        verbose_name_plural = "إعدادات التنبيهات"

    def __str__(self):
        return "إعدادات التنبيهات"



class ShipmentsSettings(models.Model):
    next_shipment_number = models.PositiveIntegerField(default=1, verbose_name="تسلسل الشحنات")
    enable_label_print = models.BooleanField(default=True, verbose_name="تفعيل طباعة الملصق")
    enable_docs_print = models.BooleanField(default=True, verbose_name="تفعيل طباعة المستندات")

    class Meta:
        verbose_name = "إعدادات الشحنات"
        verbose_name_plural = "إعدادات الشحنات"

    def __str__(self):
        return "إعدادات الشحنات"
