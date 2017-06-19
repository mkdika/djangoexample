from django import forms
from crud.models import Person


class NewPerson(forms.ModelForm):
    """
    Using manual delcare form field for detail about validation rule & custom widget.
    """



    """
    This part will use separately as auto form model base on all available field in mobel.
    """
    #birth_date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y'), input_formats = ('%m/%d/%Y',))

    class Meta():
        model = Person
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(format="%d-%m-%Y",attrs={'type': 'date',}),
            'birth_time': forms.TimeInput(format="%H:%M:%S",attrs={'type': 'time',}),
        }


