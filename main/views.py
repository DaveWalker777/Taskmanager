from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, CreateUserForm
from .decorators import *


def index(request):
    query = request.GET.get('q', '')
    if query:
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(task__icontains=query)
    else:
        tasks = Task.objects.order_by('id')[::-1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'query': query})


@login_required(login_url="login")
def about(request):
    return render(request, 'main/about.html')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you were logged in")
            return redirect('home')
        else:
            messages.error(request, "Username or password are invalid")
            return redirect('login')
    else:
        return render(request, 'main/login.html', {})


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, "you were logged out")
    return redirect('home')


@unauthenticated_user
def register_user(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'New profile was created for ' + user)
            return redirect('login')

    return render(request, 'main/register_user.html', {
        'form': form,
    })


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма содержит ошибки'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def delete_event(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def update(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/update.html', {'task': task,
                                                'form': form})



