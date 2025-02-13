from .models import Employee
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['name','email','position','department','phone','salery']


class signinForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class loginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']