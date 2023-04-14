from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create task/', views.create_task, name='create task'),
]