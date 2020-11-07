from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for '+user)
                return redirect('login')
        context={'form':form}
        return render(request,'tasks/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else: 
        if request.method == 'POST':
            username=request.POST.get('username')
            password =request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context={}
        return render(request, 'tasks/login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST) #Input by user posted on browser
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

@login_required(login_url='login')
def updateTask(request, pk): #Updating a task, receives the task name
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()     #When user updates task or mark complete, will change display in browser
            return redirect('/') #Redirects back to the main page after action


    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context) #Pass the title task into delete page
