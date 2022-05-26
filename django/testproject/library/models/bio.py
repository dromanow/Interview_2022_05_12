from django.db import models
from .author import Author


class Bio(models.Model):
    text = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text