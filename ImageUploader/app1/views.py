from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            image=form.cleaned_data['image']
            img=Image(name=name,email=email,image=image)
            img.save()
            messages.success(request, 'Image uploaded successfully')
            return redirect('view')
    form=ImageForm()
    return render(request, 'app1/index.html',context={'form':form})

def view_images(request):
    qs=Image.objects.all()
    return render(request, 'app1/list.html', context={'qs':qs})

def image_delete(request,id):
    img=Image.objects.get(pk=id)
    img.delete()
    messages.success(request, 'Image deleted successfully')
    return redirect('view')
    

def image_edit(request,id):
    img=Image.objects.get(pk=id)
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES,instance=img)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated Successfully...')
            return redirect('view')
    form=ImageForm(instance=img)
    return render(request,'app1/update.html',context={'form':form})



