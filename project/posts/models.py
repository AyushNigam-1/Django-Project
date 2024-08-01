from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User
class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, related_name='posts')
    location = models.CharField(max_length=2000)
    desc = models.CharField(max_length=10000)
    type = models.JSONField(default=list)
    posted_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField()
# Create your models here.

