from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todo=models.CharField(max_length=100)
    class Meta:
        db_table='todo'