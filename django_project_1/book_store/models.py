from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.PositiveSmallIntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
