
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task, TaskRepetition, TaskStatus


#==========================================================================================#
# >>>>> ГЛАВНАЯ СТРАНИЦА <<<<< #
#==========================================================================================#

def index(request):
    # Передача всех объектов из моделей Django.
    tasks = Task.objects.all()
    statuses = TaskStatus.objects.all()
    repetitions = TaskRepetition.objects.all()

    # Передача данных сайту.
    context = {"tasks": tasks, "status": statuses, "repetition": repetitions}

    # Открытие главной страницы.
    return render(request, "main/Index.html", context)

#==========================================================================================#
# >>>>> СТРАНИЦА, СОЗДАНИЯ НОВЫХ ЗАДАЧ <<<<< #
#==========================================================================================#

def create_task(request):
    # Если вызван метод POST.
    if request.method == 'POST':
        # Получаем данные из формы.
        formtask = TaskForm(request.POST)

        # Если данные соответвуют требованиям.
        if formtask.is_valid():
            # Сохраняем их.
            formtask.save()

            # Переходим на главную страницу.
            return redirect('Index')
        
    # Форма, без значений.    
    formtask = TaskForm()

    # Передача формы.
    context = {"formtask": formtask,
           }
    
    # Открытие страницы, создания новых задач.
    return render(request, "main/CreateTask.html", context)




