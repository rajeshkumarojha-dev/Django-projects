from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    salery = models.CharField(max_length=20)

    class Meta:
        db_table = 'employee'



    