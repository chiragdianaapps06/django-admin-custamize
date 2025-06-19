from django.db import models




class Brand(models.Model):
    name =  models.CharField(max_length=50)

    def  __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    name=models.CharField(max_length=50)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        brand_name = self.brand.name if self.brand_id else "Unassigned"
        return f"{brand_name} - {self.name}"

    

class ColorVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.color}"
    


 # from django.db import models

from django.contrib.auth.models import AbstractUser

# from .models import Brand
class User(AbstractUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('brand_admin', 'Brand Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='brand_admin')
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)



