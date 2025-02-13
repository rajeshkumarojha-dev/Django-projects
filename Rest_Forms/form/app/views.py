from django.shortcuts import render,redirect
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .form import EmployeeForm,signinForm,loginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'app/index.html')

@login_required
def emp_list(request):
    emp = Employee.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'app/list.html', context={'emp': emp})

@login_required
def emp_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user  # Set the current logged-in user
            employee.save()
            messages.success(request, 'Employee added Successfully')
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'app/add_emp.html', context={'form': form})

@login_required
def update_emp(request,id):
    emp = Employee.objects.get(pk=id, user=request.user)  # Ensure the employee belongs to the logged-in user
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated Successfully')
            return redirect('list')
    form=EmployeeForm(instance=emp)
    return render(request,'app/update.html',context={'form':form})

@login_required
def delete_emp(request,id):
    emp = Employee.objects.get(pk=id, user=request.user)  # Ensure the employee belongs to the logged-in user
    emp.delete()
    messages.success(request, 'Employee deleted Successfully')
    return redirect('list')


@api_view(['GET','POST','PUT','DELETE'])
def employee_api(request,id=None):
    if request.method=='GET':
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        else:
            emp=Employee.objects.all()
            serializer=EmployeeSerializer(emp,many=True)
            return Response(serializer.data)
        

    if request.method=='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

    if request.method=='PUT':
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(instance=emp,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
    
    if request.method=='DELETE':
        if id is not None:
            emp=Employee.objects.get(id=id)
            emp.delete()
            return Response({'message':'employee deleted successfully'})
        
    






def signin_request(request):
    if request.method=='POST':
        form=signinForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, 'User created Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Data')
    form=signinForm()
    return render(request,'registration/signin.html',context={'form':form})

def login_request(request):
    if request.method=='POST':
        form=loginForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)  
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully')
                return redirect('home')
    form=loginForm()
    return render(request,'registration/login.html',context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('login')



