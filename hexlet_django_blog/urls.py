"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Импортируем функцию include для соеденения с файлом urls.py другого приложения
from django.urls import include
# Импортируем views.py
from hexlet_django_blog import views
# Импортируем класс чтобы показать страницу
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавляем маршрут к главной странице и странице о нас
    path('', views.HomePage.as_view()),
    # Теперь мы отображаем страницу с помощью встроенного класса TemplateView и больше нет необходимости писать view функцию
    path('about/', TemplateView.as_view(template_name = 'about.html')),
    
    # Добавляем маршрут в файлу urls.py приложения article
    path('article/', include('hexlet_django_blog.article.urls')),
]
