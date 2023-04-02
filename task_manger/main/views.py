from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, )


def name(request):
    return HttpResponse("<h4>My name is Irina</h4>")
