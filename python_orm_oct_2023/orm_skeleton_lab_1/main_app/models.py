from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.CharField(max_length=30, null=True)


class Person(models.Model):
    name = models.CharField(max_length=20)


class People(models.Model):
    name = models.CharField(max_length=20)
