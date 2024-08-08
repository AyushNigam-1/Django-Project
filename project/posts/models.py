from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User
from django.conf import settings
class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='posts')
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, related_name='posts' ,blank=True) 
    applicants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users', blank=True)
    location = models.CharField(max_length=2000)
    desc = models.CharField(max_length=10000)
    posted_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.title
