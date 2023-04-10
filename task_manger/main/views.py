from django.shortcuts import render
from .models import Task, TaskRepetition, TaskStatus
from .forms import TaskForm, TaskRepetitionForm, TaskStatusForm


def index(request):
    tasks = Task.objects.order_by('id')
    statuses = TaskStatus.objects.all()
    repetitions = TaskRepetition.objects.all()
    context = {"tasks": tasks, "status": statuses, "repetition": repetitions}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")


def create_task(request):
    if request.method == 'POST':
        print(0)
        formtask = TaskForm(request.POST)
        print(12)
        if formtask.is_valid():
            print(1)
            formtask.save()
        formstatus = TaskForm(request.POST)
        if formstatus.is_valid():
            print(2)
            formstatus.save()
        formrepetition = TaskForm(request.POST)
        if formrepetition.is_valid():
            print(3)
            formrepetition.save()
    formtask = TaskForm()
    formstatus = TaskStatusForm()
    formrepetition= TaskRepetitionForm()
    context = {"formtask": formtask,
               "formstatus": formstatus,
               "formrepetition": formrepetition,
               }
    return render(request, "main/create_task.html", context)
