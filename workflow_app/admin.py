from django.contrib import admin
from .models import Workflow, WorkflowStep

class WorkflowStepInline(admin.TabularInline):
    model = WorkflowStep
    extra = 1

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):

    list_display = ("shipment", "current_status", "last_update")
    list_filter = ("current_status",)
    search_fields = ("shipment__mbl_number", "shipment__container_number")

    inlines = [WorkflowStepInline]


@admin.register(WorkflowStep)
class WorkflowStepAdmin(admin.ModelAdmin):
    list_display = ("workflow", "step_name", "timestamp")
    search_fields = ("step_name",)
