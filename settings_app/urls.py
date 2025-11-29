from django.urls import path
from .views import (
    settings_home_view,
    company_settings_view,
    alerts_settings_view,
    shipments_settings_view
)

urlpatterns = [
    path("", settings_home_view, name="settings_home"),
    path("company/", company_settings_view, name="company_settings"),
    path("alerts/", alerts_settings_view, name="alerts_settings"),
    path("shipments/", shipments_settings_view, name="shipments_settings"),
]
