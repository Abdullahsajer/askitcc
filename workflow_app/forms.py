from django import forms
from .models import Workflow, WorkflowStep

class WorkflowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ["shipment", "current_status"]
        widgets = {
            "shipment": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "current_status": forms.Select(attrs={"class": "w-full border rounded p-2"}),
        }

class WorkflowStepForm(forms.ModelForm):
    class Meta:
        model = WorkflowStep
        fields = ["step_name"]
        widgets = {
            "step_name": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
        }
