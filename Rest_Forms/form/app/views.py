from django.shortcuts import render,redirect
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .form import EmployeeForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'app/index.html')

def emp_list(request):
    emp=Employee.objects.all()
    return render(request,'app/list.html',context={'emp':emp})


def emp_form(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            data={
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'position': form.cleaned_data['position'],
                'department': form.cleaned_data['department'],
                'phone': form.cleaned_data['phone'],
                'salery': form.cleaned_data['salery']
            }

            serializer=EmployeeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, 'Employee added Successfully')
                return redirect('list')
    else:
        form=EmployeeForm()
        return render(request,'app/add_emp.html',context={'form':form})
    

def update_emp(request,id):
    emp=Employee.objects.get(pk=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated Successfully')
            return redirect('list')
    form=EmployeeForm(instance=emp)
    return render(request,'app/update.html',context={'form':form})


def delete_emp(request,id):
    emp=Employee.objects.get(id=id)
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
        
    

    

        
    