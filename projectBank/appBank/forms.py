from models import *

from django import forms
class memberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = user
        fields = ['username','password']
