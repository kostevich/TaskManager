from django.shortcuts import render, redirect
from .models import Task, TaskRepetition, TaskStatus
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    statuses = TaskStatus.objects.all()
    repetitions = TaskRepetition.objects.all()
    context = {"tasks": tasks, "status": statuses, "repetition": repetitions}
    return render(request, "main/index.html", context)



def create_task(request):
    if request.method == 'POST':
        formtask = TaskForm(request.POST)
        if formtask.is_valid():
            formtask.save()
            return redirect('index')
    formtask = TaskForm()
    context = {"formtask": formtask,
               }
    return render(request, "main/create_task.html", context)





