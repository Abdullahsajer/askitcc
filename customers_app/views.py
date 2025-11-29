from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts_app.decorators import role_required
from .models import Customer
from .forms import CustomerForm
from shipments_app.models import Shipment
from workflow_app.models import Workflow
from datetime import date, timedelta






# عرض قائمة العملاء
@role_required(["admin", "clearance"])
def customers_list_view(request):
    customers = Customer.objects.all().order_by("-id")
    return render(request, "customers/customers_list.html", {"customers": customers})

# إضافة عميل
@role_required(["admin", "clearance"])
def add_customer_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customers/")
    else:
        form = CustomerForm()

    return render(request, "customers/add_customer.html", {"form": form})


# تعديل عميل
@role_required(["admin", "clearance"])
def edit_customer_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/customers/")
    else:
        form = CustomerForm(instance=customer)

    return render(request, "customers/edit_customer.html", {"form": form, "customer": customer})

# حذف عميل
@role_required(["admin", "clearance"])
def delete_customer_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect("/customers/")


# ===============================
# صفحة عرض بيانات العميل
# ===============================
@login_required
@role_required(["admin", "clearance"])
def view_customer_view(request, customer_id):

    customer = get_object_or_404(Customer, id=customer_id)

    # حالة السجل التجاري
    cr_status = "ساري"
    if customer.cr_expiry_date:
        if customer.cr_expiry_date < date.today():
            cr_status = "منتهي"
        elif customer.cr_expiry_date <= date.today() + timedelta(days=30):
            cr_status = "قريب من الانتهاء"

    # حالة التفويض
    auth_status = "ساري"
    if customer.authorization_expiry:
        if customer.authorization_expiry < date.today():
            auth_status = "منتهي"
        elif customer.authorization_expiry <= date.today() + timedelta(days=30):
            auth_status = "قريب من الانتهاء"

    # عدد الشحنات
    shipments_count = Shipment.objects.filter(customer=customer).count()

    # عدد العمليات
    workflow_count = Workflow.objects.filter(customer=customer).count()

    # آخر 5 شحنات
    last_shipments = Shipment.objects.filter(customer=customer).order_by("-created_at")[:5]

    # آخر 5 عمليات
    last_workflows = Workflow.objects.filter(customer=customer).order_by("-created_at")[:5]

    context = {
        "customer": customer,
        "cr_status": cr_status,
        "auth_status": auth_status,
        "shipments_count": shipments_count,
        "workflow_count": workflow_count,
        "last_shipments": last_shipments,
        "last_workflows": last_workflows,
    }

    return render(request, "customers/view_customer.html", context)
