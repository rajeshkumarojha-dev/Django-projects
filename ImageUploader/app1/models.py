from django.db import models

# Create your models here.

class Image(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    image=models.ImageField(upload_to='media')
    class Meta:
        db_table='image'