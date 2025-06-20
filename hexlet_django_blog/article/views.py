from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy
from hexlet_django_blog.article.models import Article

# Create your views here.

# Создаем класс для адреса .../article
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        # Функция возвращает все объекты таблицы Article в article/index.html
        all_articles = Article.objects.all()
        return render(request, 'article/index.html', context={'articles':all_articles})


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


# Класс для показа конкретной статьи по ее id
class DefiniteArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['art_id'])
        return render(request, 'article/definite_article.html', context={'article':article})