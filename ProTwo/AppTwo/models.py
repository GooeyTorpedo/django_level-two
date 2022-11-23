from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)