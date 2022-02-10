from operator import mod
from pydoc import describe
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.
class Manufacture(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active =models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Producet(models.Model):
    manufacture = models.ForeignKey(Manufacture,on_delete=models.CASCADE,related_name='producets')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.name