from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy

# Create your views here.

# Создаем класс для адреса .../article
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={'name':'article'})


# Функция для динамического url 
# Вернет номер статьи и тег
# Кстати, неважно какой слэш поставим
def article_id_and_tag(request, article_id, tags):
    context = {
        'id':article_id,
        'tag':tags,
        'path':reverse('article', kwargs={'article_id': 0, 'tags':'Base article'})
    }
    return render(request, 'article/id_and_tag.html', context=context)