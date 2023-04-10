from .models import Task, TaskRepetition, TaskStatus
from django.forms import ModelForm, TextInput, widgets, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description")
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
                   "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи'})
                   }


class TaskStatusForm(ModelForm):
    class Meta:
        model = TaskStatus
        fields = ("status",)
        widgets = {"status": TextInput(
            attrs={'class': 'form-control', 'placeholder': 'На каком этапе решения задачи вы находитесь?'})
        }


class TaskRepetitionForm(ModelForm):
    class Meta:
        model = TaskRepetition
        fields = ("status",)
        widgets = {"status": TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Хотите выполнять задачу регулярно?'})
        }
