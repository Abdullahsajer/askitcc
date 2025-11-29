from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = "__all__"
        widgets = {
            "mbl_number": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "container_number": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "shipment_type": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "port": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "arrival_date": forms.DateInput(attrs={"type": "date", "class": "w-full border rounded p-2"}),
            "notes": forms.Textarea(attrs={"class": "w-full border rounded p-2 h-24"}),
            "customer": forms.Select(attrs={"class": "w-full border rounded p-2"}),
        }
