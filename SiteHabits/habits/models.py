from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

class Achieve(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Target(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Progress(models.Model):
    day_number = models.IntegerField()
    date = models.DateField()
    description = models.TextField()
    target = models.ForeignKey(Target, on_delete=CASCADE)