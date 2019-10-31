from django.db import models


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    image = models.BinaryField()
