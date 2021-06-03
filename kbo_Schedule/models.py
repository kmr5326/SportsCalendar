from django.db import models


class Schedule(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    game1 = models.CharField(max_length=20)
    game2 = models.CharField(max_length=20)
    game3 = models.CharField(max_length=20)
    game4 = models.CharField(max_length=20)
    game5 = models.CharField(max_length=20)
