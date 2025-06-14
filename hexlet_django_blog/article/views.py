from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Создаем класс для адреса .../article
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article\index.html', context={'name':'article'})
