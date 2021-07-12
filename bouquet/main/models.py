from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=850)
    price=models.FloatField()
    description=models.TextField()
    imglink=models.CharField(max_length=850)

class Order(models.Model):
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    address=models.CharField(max_length=850)
    city=models.CharField(max_length=400)
    payment_method=models.CharField(max_length=400)
    payment_data=models.CharField(max_length=400)
    items=models.TextField(default='')
    
    def __str__(self):
        return self.first_name


class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name