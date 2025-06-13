from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Указываем директорию, потому что создали приложение в основном пакете
    name = 'hexlet_django_blog.article'
