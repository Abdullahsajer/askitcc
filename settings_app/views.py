from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CompanySettings, AlertsSettings, ShipmentsSettings
from django.contrib.auth.decorators import login_required
from accounts_app.decorators import role_required


# صفحة الإعدادات الرئيسية
@login_required
@role_required(["admin"])
def settings_home_view(request):
    return render(request, "settings/settings_home.html")


# ------------------------------
# تعديل إعدادات الشركة
# ------------------------------
@login_required
@role_required(["admin"])
def company_settings_view(request):
    settings_obj, created = CompanySettings.objects.get_or_create(id=1)

    if request.method == "POST":
        settings_obj.company_name = request.POST.get("company_name")
        settings_obj.cr_number = request.POST.get("cr_number")
        settings_obj.vat_number = request.POST.get("vat_number")
        settings_obj.phone = request.POST.get("phone")
        settings_obj.email = request.POST.get("email")
        settings_obj.iban = request.POST.get("iban")
        settings_obj.address = request.POST.get("address")
        settings_obj.save()

        messages.success(request, "تم حفظ إعدادات الشركة بنجاح.")
        return redirect("/settings/")

    return render(request, "settings/edit_company.html", {"settings": settings_obj})


# ------------------------------
# تعديل إعدادات التنبيهات
# ------------------------------
@login_required
@role_required(["admin"])
def alerts_settings_view(request):
    settings_obj, created = AlertsSettings.objects.get_or_create(id=1)

    if request.method == "POST":
        settings_obj.notify_cr_expiry = request.POST.get("notify_cr_expiry") == "on"
        settings_obj.notify_auth_expiry = request.POST.get("notify_auth_expiry") == "on"
        settings_obj.notify_missing_docs = request.POST.get("notify_missing_docs") == "on"
        settings_obj.save()

        messages.success(request, "تم حفظ إعدادات التنبيهات بنجاح.")
        return redirect("/settings/")

    return render(request, "settings/edit_alerts.html", {"settings": settings_obj})


# ------------------------------
# تعديل إعدادات الشحنات
# ------------------------------
@login_required
@role_required(["admin"])
def shipments_settings_view(request):
    settings_obj, created = ShipmentsSettings.objects.get_or_create(id=1)

    if request.method == "POST":
        settings_obj.next_shipment_number = request.POST.get("next_shipment_number")
        settings_obj.enable_label_print = request.POST.get("enable_label_print") == "on"
        settings_obj.enable_docs_print = request.POST.get("enable_docs_print") == "on"
        settings_obj.save()

        messages.success(request, "تم حفظ إعدادات الشحنات بنجاح.")
        return redirect("/settings/")

    return render(request, "settings/edit_shipments.html", {"settings": settings_obj})
