from django.db import models

# Create your models here.
class Hydrabadjobs(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    address = models.CharField(max_length=30)
class Banglorjobs(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    address = models.CharField(max_length=30)
class Punejobs(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    address = models.CharField(max_length=30)
