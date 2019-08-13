from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=256)
# Create your models here.
