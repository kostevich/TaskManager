from .models import Task
from django.forms import ModelForm, TextInput, widgets, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description")
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
                   "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи'})
        }