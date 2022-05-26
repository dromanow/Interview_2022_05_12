from django.db import models
from .author import Author


class Book(models.Model):
    title = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
