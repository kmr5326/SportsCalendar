from django.db import models


class Schedule(models.Model):
    _id = models.CharField(max_length=20, primary_key=True)
    game1 = models.CharField(max_length=50, null=True)
    game2 = models.CharField(max_length=50, null=True)
    game3 = models.CharField(max_length=50, null=True)
    game4 = models.CharField(max_length=50, null=True)
    game5 = models.CharField(max_length=50, null=True)
    game6 = models.CharField(max_length=50, null=True)



