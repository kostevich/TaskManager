from django.db import models


class TaskStatus(models.Model):
    status = models.CharField("Статус задачи", max_length=30)

    class Meta():
        verbose_name = "Статус задачи"
        verbose_name_plural = "Все статусы задач"


class TaskRepetition(models.Model):
    status = models.CharField("Надо ли повторять задачу", max_length=30)

    class Meta():
        verbose_name = "Повторение задачи"
        verbose_name_plural = "Повторение задач"


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    creation_time = models.TimeField(auto_now_add=True)
    status = models.ManyToManyField(TaskStatus)
    repetition = models.ManyToManyField(TaskRepetition)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
