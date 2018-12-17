from django import forms
from .models import Author
from djangoexample import settings


class AuthorForm(forms.ModelForm):

    class Meta():
        model = Author
        fields = '__all__'
        widgets = {
            # 'birth_date': forms.DateInput(format='%d/%m/%Y'),
            'birth_date': forms.DateInput(format="%d-%m-%Y", attrs={'type': 'date', }),
            'join_date': forms.DateTimeInput(format="%d-%m-%Y %H:%M", attrs={'type': 'datetime', }),
            'reminder_time': forms.TimeInput(format="%H:%M", attrs={'type': 'time', }),
            'member_type': forms.RadioSelect(),
        }
