from django.db import models

# Create your models here.
class room(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length=100)