
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
   name=models.CharField(max_length=250)
   lastname=models.CharField(max_length=250)
   email=models.EmailField()
   password=models.CharField(max_length=240)
   confirm_password=models.CharField(max_length=240)
