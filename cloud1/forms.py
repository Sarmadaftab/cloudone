from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'service', 'message']

        widgets={
            'name':forms.TextInput(attrs={'placeholder':"Name"}),
            'phone_number':forms.TextInput(attrs={'placeholder':"Phone Number"}),
            'email':forms.TextInput(attrs={'placeholder':"Email"}),
            'message':forms.TextInput(attrs={'placeholder':"Write your message here"}),

        }
