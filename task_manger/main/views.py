from django.shortcuts import render
from .models import Task, TaskRepetition, TaskStatus


def index(request):
    tasks = Task.objects.all()
    statuses = TaskStatus.objects.all()
    repetitions = TaskRepetition.objects.all()
    context = {"tasks": tasks, "status": statuses, "repetition": repetitions}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")


def Python(request):
    return render(request, "main/python.html")
