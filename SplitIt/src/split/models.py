from django.db import models

# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ##slug = models.SlugField()

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)
    
class Product_List(models.Model):
    
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "$" + str(self.total)