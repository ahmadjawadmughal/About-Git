from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=50, null = True, blank=True, unique = True)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    
