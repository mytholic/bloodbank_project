from django import forms
from django.forms import fields
from django.forms import ModelForm
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model=Snippet
        fields=('name','email','phone_number','sex','blood_group','city','pre_existing_diseases')
       # pip install django-crispy-forms