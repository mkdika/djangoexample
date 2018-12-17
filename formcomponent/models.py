from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Author(models.Model):
    EDUCATION_DEGREE = (
        ('PRI', 'Primary'),
        ('INT', 'Intermediate'),
        ('HIG', 'High'),
        ('BAC', 'Bachelor Degree'),
        ('MAS', 'Master Degree'),
        ('PHD', 'Doctor Degree'),
    )

    MEMBER_TYPES = (
        ('1','REGULAR'),
        ('2','GOLD'),
        ('3','PLATINUM')
    )

    # name, TextField
    name = models.CharField(max_length=100, unique=True)

    # birth_date, DateField
    birth_date = models.DateField()

    # last_education, ChoiceField (ComboBox)
    last_education = models.CharField(
        max_length=3,
        choices=EDUCATION_DEGREE,
        default='HIG',
        null=True
    )

    # join_date, DateTimeField
    join_date = models.DateTimeField(default=datetime.now)

    # reminder_time, TimeField
    reminder_time = models.TimeField()

    # email, TextField (Email Validation)
    email = models.EmailField(null=True)

    # website, TextField (URL validation)
    website = models.URLField(null=True)

    # address, TextArea
    address = models.TextField(null=True)

    # member_type, RadioField (Single Choices)
    member_type = models.CharField(
        max_length=20,
        choices=MEMBER_TYPES,
        default='1'
    )

    # term_day, IntegerField
    term_day = models.IntegerField(default=30)

    # balance, DecimalField
    balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    # active, BooleanField (single)
    active = models.BooleanField(default=True)

    # bio, RichTextField (WYSIWYG)
    bio = RichTextField(blank=True)
    
    class Meta:
        db_table = 'tb_author'
