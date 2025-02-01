from django.db import models


# Create your models here.
class NavItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField() 
    active = models.BooleanField(default=True)  
    active = models.BooleanField(default=True)  
    
    def __str__(self):
      return self.name


class Formulation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, default='')  # Store password securely with hashing

    def __str__(self):
        return self.email
