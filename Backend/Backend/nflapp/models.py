from django.db import models

class Game(models.Model):
    gameid = models.CharField(max_length=200)
    week_year = models.CharField(max_length=200)
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)

class Link(models.Model):
    similar_game = models.CharField(max_length=200)
    box_score = models.CharField(max_length=400)
    highlights = models.CharField(max_length=400, default=None)
    

