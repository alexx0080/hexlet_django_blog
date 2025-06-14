# Это нами созданный файл для вьюх

from django.shortcuts import render
from django.views.generic.base import TemplateView


# Главная страница теперь реализована с помощью класса
class HomePage(TemplateView):
    template_name = 'index.html'

    # Встроенная функция возвращает контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'who': 'world'}
        return context


# Страница о нас
def about(request):
    return render(request, 'about.html')


# Тест для динамический url
def dinamyc_url(request, number):
    context = {'number':number}
    return render(request, 'numbers.html', context=context)

