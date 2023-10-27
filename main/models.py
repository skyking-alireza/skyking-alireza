from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customers(AbstractUser):
    level = models.IntegerField(default=0, null=True, blank=True)
    avatar = models.CharField(blank=True, default='7294787.jpg', max_length=150)


class Cryptos(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Amount(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='customer')
    crypto = models.ForeignKey(Cryptos, on_delete=models.CASCADE, related_name='crypto')
    value = models.FloatField()
