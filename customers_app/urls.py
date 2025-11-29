from django.urls import path
from .views import (
    customers_list_view,
    add_customer_view,
    edit_customer_view,
    delete_customer_view,
    view_customer_view,
)
from accounts_app.decorators import permission_required

app_name = "customers_app"

urlpatterns = [
    path("", 
         permission_required("customers.view_customer")(customers_list_view),
         name="list"),

    path("add/",
         permission_required("customers.add_customer")(add_customer_view),
         name="add"),

    path("edit/<int:customer_id>/",
         permission_required("customers.edit_customer")(edit_customer_view),
         name="edit"),

    path("delete/<int:customer_id>/",
         permission_required("customers.delete_customer")(delete_customer_view),
         name="delete"),

    path("view/<int:customer_id>/",
         permission_required("customers.view_customer")(view_customer_view),
         name="view_customer"),
]
