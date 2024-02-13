from django.db import models

# Create your models here.

class Item(models.Model):
    itemname = models.TextField(max_length=100)
    amount = models.CharField(max_length=100)
    bought_from= models.CharField(blank=True,max_length=10)
    bought_on = models.DateField(blank=True, auto_now=False, auto_now_add=False)
    price = models.IntegerField(blank=True, max_length=15,default="")
    ref = models.FloatField(blank=True)

    
    
    


