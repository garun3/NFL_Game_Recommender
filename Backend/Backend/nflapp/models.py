from django.db import models

class Game(models.Model):
    week = models.IntegerField(default=0)
    day = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    winner = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    loser = models.CharField(max_length=200)
    PtsW = models.IntegerField(default=0)
    PtsL = models.IntegerField(default=0)
    YdsW = models.IntegerField(default=0)
    TOW = models.IntegerField(default=0)
    YdsL = models.IntegerField(default=0)
    TOL = models.IntegerField(default=0)

class Link(models.Model):
    similar_game = models.CharField(max_length=200)
    box_score = models.CharField(max_length=400)
    highlights = models.CharField(max_length=400, default=None)

