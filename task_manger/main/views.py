from django.shortcuts import render
from .models import Task, TaskRepetition, TaskStatus


def index(request):
    task = Task.objects.all()
    status = TaskStatus.objects.all()
    repetition = TaskRepetition.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница'}, {'tasks': task})


def about(request):
    return render(request, "main/about.html")


def Python(request):
    return render(request, "main/python.html")

