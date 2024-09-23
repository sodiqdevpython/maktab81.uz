from django import forms
from .models import Contact

class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fio', 'tel_number', 'body']