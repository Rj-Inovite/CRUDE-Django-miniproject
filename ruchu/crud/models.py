from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    facescan= models.CharField(max_length=255, default='default.jpg')
    