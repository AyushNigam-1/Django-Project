from django.db import models
from django.contrib.auth.models import User

class Metadata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.user.username
