from django.shortcuts import render,redirect
from .forms import TodoForm,SignInForm,LogInForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'app/index.html')

@login_required
def todo_request(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            form=TodoForm()
            return redirect('/todo')
            
    else:
        form=TodoForm()
        todo=Todo.objects.filter(user=request.user)
        return render(request,'app/todo.html',context={'form':form,'todo':todo})

@login_required
def update_request(request,id):
    qs=Todo.objects.get(pk=id,user=request.user)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            form=TodoForm()
            return redirect('todo')
    form=TodoForm(instance=qs)
    return render(request,'app/update.html',context={'form':form})

@login_required
def delete_request(request,id):
    todo=Todo.objects.get(pk=id,user=request.user)
    todo.delete()
    return redirect('todo')

@login_required
def list_request(request):
    todo=Todo.objects.filter(user=request.user)
    return render(request,'app/list.html',context={'todo':todo})


def SignIn_request(request):
    if request.method=='POST':
        form=SignInForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'Register Successfully...')
            form=SignInForm()
            return redirect('home')
        else:
            messages.error(request, "Error in registration. Please try again.")
    form=SignInForm()
    return render(request,'registration/signin.html',context={'form':form})

def login_request(request):
    if request.method=='POST':
        form=LogInForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Login Successfully...')
                form=LogInForm()
                return redirect('home')
        else:
            messages.error(request, "Check Username and Password")
    form=LogInForm()
    return render(request,'registration/login.html',context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('login')