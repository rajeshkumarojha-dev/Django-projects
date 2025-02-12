from .models import Employee
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['name','email','position','department','phone','salery']