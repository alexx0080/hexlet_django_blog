# Это нами созданный файл для вьюх

from django.shortcuts import render


# Главная страница
def index(request):
    return render(request, 'index.html', context={'who':'world'})


# Страница о нас
def about(request):
    return render(request, 'about.html')

