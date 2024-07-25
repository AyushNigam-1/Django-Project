from django.db import models
from categories.models import Categories
class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    location = models.CharField(max_length=2000)
    desc = models.IntegerField(default=0)
    type =models.JSONField(default=list)
    applicants = models.CharField(max_length=1000)
    posted_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField()
# Create your models here.

