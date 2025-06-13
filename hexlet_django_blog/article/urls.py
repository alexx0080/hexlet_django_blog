# Созданный нами urls.py для приложения

from django.urls import path
# Импортируем views.py нашего приложения
from hexlet_django_blog.article import views


urlpatterns = [
    # Это адрес .../article
    path('', views.index),
]
