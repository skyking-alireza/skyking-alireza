from django.db import models

# Create your models here.
class PageModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        ordering = ['-id']