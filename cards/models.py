from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=60)
    set = models.CharField(max_length=80)
    number = models.IntegerField(default=0)
