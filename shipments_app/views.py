from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment
from .forms import ShipmentForm

# قائمة الشحنات
def shipments_list_view(request):
    shipments = Shipment.objects.all().order_by("-id")
    return render(request, "shipments/shipments_list.html", {"shipments": shipments})

# إضافة شحنة
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
def delete_shipment_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    shipment.delete()
    return redirect("/shipments/")
