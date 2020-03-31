from django.db import models

from django.contrib.auth.models import User


class Article(models.Model):
    """Custom Model for storing articles."""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of Article"""
        return self.title

    def snippet(self):
        """Returns a part of the body for the Aritcles List page"""
        return (self.body[:50] + "...")# Using string slicing
