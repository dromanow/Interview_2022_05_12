from django.db import models
from .author import Author

from django.db.models import Manager


class DeletedQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(deleted=False)

    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Bio(models.Model):
    text = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False, null=False)
    objects = DeletedManager()

    def __str__(self):
        return self.text
