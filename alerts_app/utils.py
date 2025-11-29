from datetime import date, timedelta
from customers_app.models import Customer
from shipments_app.models import Shipment
from workflow_app.models import Workflow

def get_alerts():
    alerts = []
    today = date.today()

    # انتهاء السجل التجاري
    exp_cr = Customer.objects.filter(cr_expiry_date__lte=today + timedelta(days=30))
    for c in exp_cr:
        alerts.append({
            "type": "warning",
            "message": f"انتهاء السجل التجاري للعميل {c.name} بتاريخ {c.cr_expiry_date}"
        })

    # انتهاء التفويض
    exp_auth = Customer.objects.filter(authorization_expiry__lte=today + timedelta(days=30))
    for c in exp_auth:
        alerts.append({
            "type": "warning",
            "message": f"انتهاء التفويض للعميل {c.name} بتاريخ {c.authorization_expiry}"
        })

    # الشحنات القادمة خلال 3 أيام
    incoming = Shipment.objects.filter(arrival_date__lte=today + timedelta(days=3))
    for s in incoming:
        alerts.append({
            "type": "info",
            "message": f"الشحنة {s.container_number} ستصل خلال 3 أيام"
        })

    # جاهزة للسحب
    ready = Workflow.objects.filter(current_status="ready")
    for w in ready:
        alerts.append({
            "type": "success",
            "message": f"الشحنة {w.shipment.container_number} جاهزة للسحب"
        })

    return alerts
