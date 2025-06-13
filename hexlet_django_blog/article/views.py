from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Создаем функцию для адреса .../article
def index(request):
    return HttpResponse('article')