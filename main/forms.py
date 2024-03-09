from .models import Task, Theme
from django.forms import ModelForm, TextInput, Textarea, TimeInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "time", "date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату DD.MM.YYYY'
            }),
            "time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите время HH:MM'
            })

        }


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['title']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
