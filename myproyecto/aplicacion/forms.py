from django import forms
from .models import PrimaryContact, SecondaryContact

class PrimaryContactForm(forms.ModelForm):
    class Meta:
        model = PrimaryContact
        fields = ['name', 'email', 'message']

class SecondaryContactForm(forms.ModelForm):
    class Meta:
        model = SecondaryContact
        fields = ['name', 'email', 'message']