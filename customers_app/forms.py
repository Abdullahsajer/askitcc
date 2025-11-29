from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'cr_number': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'cr_expiry_date': forms.DateInput(attrs={'class': 'w-full border rounded p-2', 'type': 'date'}),
            'authorization_number': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'authorization_expiry': forms.DateInput(attrs={'class': 'w-full border rounded p-2', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border rounded p-2'}),
            'notes': forms.Textarea(attrs={'class': 'w-full border rounded p-2 h-24'}),
        }
