from django.contrib import admin
from hexlet_django_blog.article.models import Article
from django.contrib.admin import DateFieldListFilter
# Register your models here.

# Сделаем поиск по статьям
# Прикольная штука, позволяет в админке вбивать строку в поиск и ищет эту подстроку в указанных полях
# В данном случае name и body
class AdminArticle(admin.ModelAdmin):
    # Перечисляем поля, отображаемые в таблице списка статей, метод __str__ можно не использовать если используем это
    list_display = ('id', 'name', 'created_at')
    # Перечисляем поля по которым производится поиск
    search_fields = ['name', 'body']
    list_filter = (('created_at', DateFieldListFilter),)


# Зарегестрируем модели
admin.site.register(Article, AdminArticle)


# Можно сделать подругому и улучшить читаемость кода:

# @admin.register(Article)
# class AdminArticle(admin.ModelAdmin):
#     search_fields = ['name', 'body']

# Но мне больше нравится первый вариант, он попонятнее