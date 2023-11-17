from django.db import models

# Create your models here.
class RealEsModel(models.Model):
    Title=models.CharField(default="",max_length=100)
    Description=models.CharField(default="",max_length=100)
    Price=models.CharField(default="",max_length=100)
    Property=models.CharField(default="",max_length=100)
    Location=models.CharField(default="",max_length=100)
    Bedroom=models.CharField(default="",max_length=100)
    Bathrooms=models.CharField(default="",max_length=100)