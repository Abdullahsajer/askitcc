from django.urls import path
from .views import (
    shipments_list_view,
    add_shipment_view,
    edit_shipment_view,
    delete_shipment_view,
)
from accounts_app.decorators import permission_required

app_name = "shipments_app"

urlpatterns = [
    path("",
         permission_required("shipments.view_shipment")(shipments_list_view),
         name="list"),

    path("add/",
         permission_required("shipments.add_shipment")(add_shipment_view),
         name="add"),

    path("edit/<int:shipment_id>/",
         permission_required("shipments.edit_shipment")(edit_shipment_view),
         name="edit"),

    path("delete/<int:shipment_id>/",
         permission_required("shipments.delete_shipment")(delete_shipment_view),
         name="delete"),
]
