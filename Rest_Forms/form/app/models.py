from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    position=models.CharField(max_length=40)
    department=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    salery=models.CharField(max_length=20)
    class Meta:
        db_table='employee'


