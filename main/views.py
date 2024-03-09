from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, Theme
from .forms import TaskForm, CreateUserForm, ThemeForm
from .decorators import *


def index(request):
    query = request.GET.get('q', '')
    if query:
        themes = Theme.objects.filter(title__icontains=query)
    else:
        themes = Theme.objects.order_by('id')[::-1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'themes': themes, 'query': query})


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
def create(request, theme_id):
    error = ''
    theme = Theme.objects.get(pk=theme_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.theme = theme
            form.save()
            return redirect('home')
        else:
            return render(request, 'main/create.html', {'form': form,
                                                        'theme': theme})
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def add_theme(request):
    error = ''
    if request.method == 'POST':
        theme_form = ThemeForm(request.POST)
        if theme_form.is_valid():
            theme_form.save()
            return redirect('home')
        else:
            return render(request, 'main/add_theme.html', {'theme_form': theme_form})
    theme_form = ThemeForm()
    context = {
        'theme_form': theme_form,
        'error': error
    }
    return render(request, 'main/add_theme.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def delete_event(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin', 'editor'])
def delete_theme(request, theme_id):
    theme = Theme.objects.get(pk=theme_id)
    theme.delete()
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



