from django.db import models

class Link(models.Model):
    similar_game = models.CharField(max_length=200)
    box_score = models.CharField(max_length=400)
    highlights = models.CharField(max_length=400, default=None)
    

