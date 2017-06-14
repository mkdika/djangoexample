from django.db import models

# Create your models here.
class Person(models.Model):
    EDUCATION_DEGREE = (
        ('SD', 'Primary'),
        ('SMP', 'Intermediate'),
        ('SMU', 'High'),
        ('S1', 'Bachelor Degree'),
        ('S2', 'Master Degree'),
        ('S3', 'Doctor Degree'),
    )

    class Meta:
        db_table = 'tb_person' # custom database table name rather than to user class name.

    uid = models.CharField(max_length=100, unique=True,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_male = models.BooleanField()
    birth_date = models.DateField()
    birth_time = models.TimeField()
    registration_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    height = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    last_education = models.CharField(
        max_length=3,
        choices=EDUCATION_DEGREE,
        default='SMU',
        null=True
    )
    photo = models.BinaryField(null=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name