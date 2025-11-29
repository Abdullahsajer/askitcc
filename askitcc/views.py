from django.shortcuts import render
from customers_app.models import Customer
from shipments_app.models import Shipment
from transport_app.models import TransportTask
from workflow_app.models import Workflow
from alerts_app.utils import get_alerts
from alerts_app.context_processors import alerts_context




def dashboard_view(request):

    context = {
        "customers_count": Customer.objects.count(),
        "shipments_count": Shipment.objects.count(),
        "transport_count": TransportTask.objects.count(),
        "workflow_active": Workflow.objects.filter(current_status__in=["customs", "documents"]).count(),
        "workflow_ready": Workflow.objects.filter(current_status="ready").count(),
        "recent_shipments": Shipment.objects.order_by("-id")[:5],
    }
    context.update(alerts_context(request))
    
    return render(request, "dashboard/index.html", context)
