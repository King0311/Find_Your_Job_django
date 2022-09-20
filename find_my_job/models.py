import email
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class hr_profile(models.Model):
    username=models.CharField(default="", max_length=50)
    personal_name=models.CharField( default="", max_length=50)
    company_name=models.CharField(default="", max_length=50)
    email=models.EmailField(default="", max_length=254)
    company_city=models.CharField(default="", max_length=50)
    post=models.CharField(default="", max_length=50)

class seeker_profile(models.Model):
    username=models.CharField(default="", max_length=50)
    name=models.CharField(default="", max_length=50)
    current_company_name=models.CharField(default="", max_length=50)
    email=models.EmailField(default="", max_length=254)
    profession=models.CharField(default="", max_length=50)
