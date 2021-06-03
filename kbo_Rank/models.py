from django.db import models


class Rank(models.Model):
    rank = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    gameCnt = models.CharField(max_length=20)
    win = models.CharField(max_length=20)
    lose = models.CharField(max_length=20)
    draw = models.CharField(max_length=20)