from django.contrib import admin
from .models import Task, TaskStatus, TaskRepetition


admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(TaskRepetition)