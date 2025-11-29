from django.urls import path
from .views import (
    transport_list_view,
    add_transport_view,
    edit_transport_view,
    delete_transport_view,
)

app_name = "transport_app"

urlpatterns = [
    path("", transport_list_view, name="list"),
    path("add/", add_transport_view, name="add"),
    path("edit/<int:task_id>/", edit_transport_view, name="edit"),
    path("delete/<int:task_id>/", delete_transport_view, name="delete"),
]
