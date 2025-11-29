from django.urls import path
from .views import (
    transport_list_view,
    add_transport_view,
    edit_transport_view,
    delete_transport_view,
)
from accounts_app.decorators import permission_required

app_name = "transport_app"

urlpatterns = [
    path("",
         permission_required("transport.view_transport")(transport_list_view),
         name="list"),

    path("add/",
         permission_required("transport.add_transport")(add_transport_view),
         name="add"),

    path("edit/<int:task_id>/",
         permission_required("transport.edit_transport")(edit_transport_view),
         name="edit"),

    path("delete/<int:task_id>/",
         permission_required("transport.delete_transport")(delete_transport_view),
         name="delete"),
]
