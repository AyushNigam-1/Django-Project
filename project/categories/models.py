from django.db import models
class Categories(models.Model):
    name = models.CharField(max_length=50)
    counts = models.IntegerField()
    desc = models.TextField()
    icon = models.CharField(max_length=1000)
# Create your models here.
