from rest_framework import serializers
from .models import Employee

class empSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'phone', 'salery']
    