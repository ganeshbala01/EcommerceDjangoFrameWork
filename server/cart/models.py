from django.db import models




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.DecimalField(max_digits=10, decimal_places=2)

