
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from .models import Task
from django import forms
from django.forms import TextInput, Textarea

#==========================================================================================#
# >>>>> СОЗДАНИЕ ФОРМЫ <<<<< #
#==========================================================================================#

class TaskForm(forms.ModelForm):
    class Meta:
        # Использование модели.
        model = Task

        # Использование полей модели.
        fields = ("title", "description", "status", "repetition",)

        # Вывод пустых полей формы.
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
                   "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание задачи'}),}
        

        # Вывод пустых полей формы.
        status = forms.MultipleChoiceField
        repetitions = forms.MultipleChoiceField


