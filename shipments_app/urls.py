from django.urls import path
from .views import (
    shipments_list_view,
    add_shipment_view,
    edit_shipment_view,
    delete_shipment_view,
)

app_name = "shipments_app"

urlpatterns = [
    path("", shipments_list_view, name="list"),
    path("add/", add_shipment_view, name="add"),
    path("edit/<int:shipment_id>/", edit_shipment_view, name="edit"),
    path("delete/<int:shipment_id>/", delete_shipment_view, name="delete"),
]
