from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000)
    desc = models.CharField(max_length=10000)
    posts = models.ForeignKey("posts.Post", on_delete=models.CASCADE , related_name='posts')
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    fb_id = models.CharField(max_length=100)
    ld_id = models.CharField(max_length=100)
    x_id = models.CharField(max_length=100)
    ig_id = models.CharField(max_length=100)
    
    

# Create your models here.
