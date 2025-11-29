from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts_app.decorators import permission_required
from .models import Shipment
from .forms import ShipmentForm


# قائمة الشحنات
@login_required
@permission_required("shipments.view_shipment")
def shipments_list_view(request):
    shipments = Shipment.objects.all().order_by("-id")
    return render(request, "shipments/shipments_list.html", {"shipments": shipments})


# إضافة شحنة
@login_required
@permission_required("shipments.add_shipment")
def add_shipment_view(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/shipments/")
    else:
        form = ShipmentForm()

    return render(request, "shipments/add_shipment.html", {"form": form})


# تعديل شحنة
@login_required
@permission_required("shipments.edit_shipment")
def edit_shipment_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)

    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect("/shipments/")
    else:
        form = ShipmentForm(instance=shipment)

    return render(request, "shipments/edit_shipment.html", {"form": form, "shipment": shipment})


# حذف شحنة
@login_required
@permission_required("shipments.delete_shipment")
def delete_shipment_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    shipment.delete()
    return redirect("/shipments/")
