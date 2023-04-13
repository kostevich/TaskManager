from .models import Task, TaskStatus, TaskRepetition
from django import forms
from django.forms import TextInput, Textarea


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "status", "repetition",)
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
                   "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи'})}


        status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,)
        repetitions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,)

