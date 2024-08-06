from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000)
    desc = models.CharField(max_length=10000)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    fb_id = models.CharField(max_length=100)
    ld_id = models.CharField(max_length=100)
    x_id = models.CharField(max_length=100)
    ig_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
