from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=54)
    roll=models.IntegerField()
    city=models.CharField(max_length=76)