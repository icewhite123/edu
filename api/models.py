from django.db import models

# Create your models here.

class News(models.Model):
    text = models.CharField(max_length=30)