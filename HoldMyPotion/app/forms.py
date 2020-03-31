from django import forms

from . import models


class CreateArticle(forms.ModelForm):
    """Form field to create an article through front-end"""
    class Meta:
        model = models.Article
        fields = ['title','body', 'slug', 'thumb',]
