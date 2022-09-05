from django.db import models

# Create your models here.
class scoreboard(models.Model):
    na=models.CharField(max_length=20)
    sc=models.IntegerField()
