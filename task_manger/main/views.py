from django.shortcuts import render
from .models import Task, TaskRepetition, TaskStatus
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    statuses = TaskStatus.objects.all()
    repetitions = TaskRepetition.objects.all()
    context = {"tasks": tasks, "status": statuses, "repetition": repetitions}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")


def create_task(request):
    form = TaskForm()
    context = {"form": form}
    return render(request, "main/create_task.html", context)
