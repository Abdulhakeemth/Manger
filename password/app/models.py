from django.db import models
# Create your models here
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    country = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.country

class State(models.Model):
    countryid = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    state = models.CharField(max_length=30,null=True)   
    def __str__(self):
        return self.state

class Userwait(models.Model):
    GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
    )

    stateid = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    username =   models.CharField(max_length=30,null=True,unique=True)      
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length = 10,choices = GENDER_CHOICES)
    email = models.EmailField(max_length=50,null=True)
    empimage = models.ImageField(null=True,default='default.webp')
    password = models.CharField(max_length=50,null=True)    
    def __str__(self):
         return self.username

