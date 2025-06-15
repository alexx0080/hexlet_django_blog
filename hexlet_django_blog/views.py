# Это нами созданный файл для вьюх

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


# Главная страница теперь реализована с помощью класса
# class HomePage(TemplateView):
#     template_name = 'index.html'

#     # Встроенная функция возвращает контекст
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = {'who': 'world'}
#         return context
    

# Новая фукнция для главной страницы
def index(request):
    # Перенаправляем на эту директорию
    return redirect(reverse('article', kwargs={'article_id':42, 'tags':'python'}))


# Страница о нас но сейчас в ней нет необходимости, так как ее показывают через встроенный класс
# def about(request):
#     return render(request, 'about.html')


