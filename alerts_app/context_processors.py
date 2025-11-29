from datetime import date, timedelta
from customers_app.models import Customer
from settings_app.models import AlertsSettings


def alerts_context(request):
    """إرجاع عدد التنبيهات + قائمة آخر التنبيهات."""

    alerts_settings = AlertsSettings.objects.first()

    alerts = []

    # إذا لم يتم إنشاء إعدادات التنبيهات — لا تعمل أي تنبيهات
    if not alerts_settings:
        return {"alerts": [], "alerts_count": 0}

    # -----------------------------------------------------
    # 1) تنبيه انتهاء السجل التجاري (CR Expiry)
    # -----------------------------------------------------
    if alerts_settings.notify_cr_expiry:
        soon = date.today() + timedelta(days=30)

        expiring_cr = Customer.objects.filter(cr_expiry_date__lte=soon)

        for cust in expiring_cr:
            alerts.append({
                "type": "warning",
                "message": f"السجل التجاري للعميل ({cust.name}) سينتهي قريباً.",
            })

    # -----------------------------------------------------
    # 2) تنبيه انتهاء التفويض Authorization
    # -----------------------------------------------------
    if alerts_settings.notify_auth_expiry:
        soon = date.today() + timedelta(days=30)

        expiring_auth = Customer.objects.filter(authorization_expiry__lte=soon)

        for cust in expiring_auth:
            alerts.append({
                "type": "warning",
                "message": f"تفويض العميل ({cust.name}) سينتهي قريباً.",
            })

    # -----------------------------------------------------
    # 3) تنبيه نقص المستندات (كخيار إضافي للتوسع)
    # -----------------------------------------------------
    if alerts_settings.notify_missing_docs:
        customers = Customer.objects.all()
        for cust in customers:
            if not cust.cr_number or not cust.authorization_number:
                alerts.append({
                    "type": "info",
                    "message": f"العميل ({cust.name}) لديه مستندات ناقصة.",
                })

    # ترتيب التنبيهات
    alerts = alerts[:10]

    return {
        "alerts": alerts,
        "alerts_count": len(alerts),
    }
