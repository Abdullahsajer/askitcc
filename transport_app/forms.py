from django import forms
from .models import TransportTask

class TransportForm(forms.ModelForm):
    class Meta:
        model = TransportTask
        fields = "__all__"
        widgets = {
            "shipment": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "task_type": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "driver_name": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "task_date": forms.DateInput(attrs={"type": "date", "class": "w-full border rounded p-2"}),
            "notes": forms.Textarea(attrs={"class": "w-full border rounded p-2 h-24"}),
            "status": forms.Select(attrs={"class": "w-full border rounded p-2"}),
        }
