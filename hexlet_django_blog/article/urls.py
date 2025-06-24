# Созданный нами urls.py для приложения

from django.urls import path
# Импортируем views.py нашего приложения
from hexlet_django_blog.article import views


urlpatterns = [
    # Это адрес .../article 
    path('', views.ArticleView.as_view(), name='all_articles'),
    # Динамический url
    path('<str:tags>/<int:article_id>/', views.article_id_and_tag, name='article'),
    # Добавляем маршрут показа статьи по ее номеру
    path('<int:art_id>/', views.DefiniteArticle.as_view(), name='definite_article'),
    # Добавляем маршрут для создания статьи с помощью формы
    path('create/', views.ArticleFormCreateView.as_view(), name='create_article'),
]
