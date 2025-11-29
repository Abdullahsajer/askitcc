from django.urls import path
from .views import alerts_list_view

app_name = "alerts_app"

urlpatterns = [
    path("", alerts_list_view, name="alerts"),
]
