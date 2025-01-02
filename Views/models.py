from django.db import models

# Create your models here.

class model_form(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()