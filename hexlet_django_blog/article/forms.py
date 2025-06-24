from django import forms
from django.forms import ModelForm
from hexlet_django_blog.article import models


class ArticleForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ['name', 'body']