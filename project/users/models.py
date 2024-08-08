from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    document = models.FileField(upload_to='user_documents/', blank=True, null=True)

    def __str__(self):
        return self.username
