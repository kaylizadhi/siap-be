# accounts/forms.py
from django import forms
from .models import buatAkun

class FormBuatAkun(forms.ModelForm):
    class Meta:
        model = BuatAkun
        fields = ['name', 'email','role','password', 'security_question', 'security_answer']
