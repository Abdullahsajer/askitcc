from django.urls import path
from .views import (
    settings_home_view,
    company_settings_view,
    alerts_settings_view,
    shipments_settings_view
)
from accounts_app.decorators import permission_required

app_name = "settings_app"

urlpatterns = [
    path("",
         permission_required("settings.view_settings")(settings_home_view),
         name="settings_home"),

    path("company/",
         permission_required("settings.edit_settings")(company_settings_view),
         name="company_settings"),

    path("alerts/",
         permission_required("settings.edit_settings")(alerts_settings_view),
         name="alerts_settings"),

    path("shipments/",
         permission_required("settings.edit_settings")(shipments_settings_view),
         name="shipments_settings"),
]
