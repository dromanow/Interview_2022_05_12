from django.db import models
from django.db.models import Manager

from .author import Author
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Book(models.Model):
    title = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')
    # objects = CurrentSiteManager('site')

    def __str__(self):
        return self.title
