from django.db import models
from main.models import Customers
# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_created=True,auto_now_add=True)
    like = models.IntegerField(blank=True,null=True)
    image = models.CharField(max_length=150)
    
    class Meta:
        ordering  =  ['-id']

class BlogCommentModel(models.Model):
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    user = models.ForeignKey(Customers , on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    body = models.CharField(max_length=500)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    stars = models.IntegerField()
