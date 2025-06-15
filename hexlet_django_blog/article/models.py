from django.db import models

# Create your models here.

# Для создания таблицы в базе данных нужно в терминале написать python manage.py makemigrations
# Для последующих изменений использовать migrate
# Посмотреть все миграции можно в папке migrations приложения
# Посмотреть sql запрос можно командой sqlmigrate имя_приложение номер_миграции
# Настройки базы данных в settings.py

# Создаем модель Article
class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
