from operator import mod
from unicodedata import name
from django.db import models


# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100, null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name=models.CharField(max_length=100, null=False)
    last_name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.CharField(max_length=100)
    phone=models.IntegerField(default=0)
    date=models.DateField()
    
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)
    

