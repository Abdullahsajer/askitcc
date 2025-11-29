from django.shortcuts import render
from .utils import get_alerts

def alerts_list_view(request):
    return render(request, "alerts/alerts_list.html", {"alerts": get_alerts()})
