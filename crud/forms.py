from django import forms
from django.core import validators
from crud.models import Person

class NewPerson(forms.ModelForm):
    class Meta():
        model = Person
        fields = '__all__'