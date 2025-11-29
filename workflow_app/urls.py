from django.urls import path
from .views import (
    workflow_list_view,
    add_workflow_view,
    workflow_detail_view,
    add_step_view,
    edit_workflow_view,
    delete_workflow_view,
    delete_step_view,
)

app_name = "workflow_app"

urlpatterns = [
    path("", workflow_list_view, name="list"),
    path("add/", add_workflow_view, name="add"),
    path("<int:workflow_id>/", workflow_detail_view, name="detail"),
    path("<int:workflow_id>/add-step/", add_step_view, name="add_step"),
    path("<int:workflow_id>/edit/", edit_workflow_view, name="edit"),
    path("<int:workflow_id>/delete/", delete_workflow_view, name="delete"),
    path("delete-step/<int:step_id>/", delete_step_view, name="delete_step"),
]
