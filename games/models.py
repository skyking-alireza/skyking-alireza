from django.db import models

# Create your models here.
class game(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=150)