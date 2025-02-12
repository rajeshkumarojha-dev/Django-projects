from django.shortcuts import render,redirect
from django.contrib import messages
from .serializers import empSerializer
from .models import Employee
from rest_framework.decorators import api_view
from .form import EmpForm
from rest_framework.response import Response
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'department': form.cleaned_data['department'],
                'phone': form.cleaned_data['phone'],
                'salery': form.cleaned_data['salery'],
            }
            serializer=empSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, 'Employee added successfully')
                return redirect('home')
        
    else:
        form = EmpForm()
    return render(request, 'app/home.html', context={'form': form})

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'app/emp_list.html', context={'employees': employees})

def update_emp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmpForm(instance=emp)
    if request.method == 'POST':
        form = EmpForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully')
            return redirect('emp_list')
    return render(request, 'app/update.html', context={'form': form})

def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    messages.success(request, 'Employee deleted successfully')
    return redirect('emp_list')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def emp_api(request):
    if request.method == 'GET':  # Fetch all students
        students = Employee.objects.all()
        serializer = empSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Create a new student
        serializer = empSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':  # Update a student
        student = Employee.objects.get(id=request.data['id'])
        serializer = empSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':  # Delete a student    
        student = Employee.objects.get(id=request.data['id'])
        student.delete()
        return Response({'message': 'Student deleted successfully'})

