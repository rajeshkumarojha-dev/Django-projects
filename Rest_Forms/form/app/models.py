from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    position=models.CharField(max_length=40)
    department=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    salery=models.CharField(max_length=20)
    class Meta:
        db_table='employee'


