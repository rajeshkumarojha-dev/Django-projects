from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    context = {
        'name': user.first_name,
        'profile_picture': user.socialaccount_set.filter(provider='google').first().extra_data['picture']
    }
    return render(request,'app1/home.html',context)

def home(request):
    return render(request,'app1/index.html') 

def logout_view(request):
    logout(request)
    return redirect('home')