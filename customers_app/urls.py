from django.urls import path
from .views import (
    customers_list_view,
    add_customer_view,
    edit_customer_view,
    delete_customer_view,
    view_customer_view,)

app_name = "customers_app"

urlpatterns = [
    path("", customers_list_view, name="list"),
    path("add/", add_customer_view, name="add"),
    path("edit/<int:customer_id>/", edit_customer_view, name="edit"),
    path("delete/<int:customer_id>/", delete_customer_view, name="delete"),
    path("view/<int:customer_id>/", view_customer_view, name="view_customer"),

]
