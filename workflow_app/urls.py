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
from accounts_app.decorators import permission_required

app_name = "workflow_app"

urlpatterns = [
    path("",
         permission_required("workflow.view_workflow")(workflow_list_view),
         name="list"),

    path("add/",
         permission_required("workflow.add_workflow")(add_workflow_view),
         name="add"),

    path("<int:workflow_id>/",
         permission_required("workflow.view_workflow")(workflow_detail_view),
         name="detail"),

    path("<int:workflow_id>/add-step/",
         permission_required("workflow.edit_workflow")(add_step_view),
         name="add_step"),

    path("<int:workflow_id>/edit/",
         permission_required("workflow.edit_workflow")(edit_workflow_view),
         name="edit"),

    path("<int:workflow_id>/delete/",
         permission_required("workflow.delete_workflow")(delete_workflow_view),
         name="delete"),

    path("delete-step/<int:step_id>/",
         permission_required("workflow.delete_workflow")(delete_step_view),
         name="delete_step"),
]
