from django.db import models

# Create your models here.
class Beverage(models.Model):
    code = models.CharField(max_length=4)
    type = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.code} ({self.type})"
    
class Drink(models.Model):
    category = models.ForeignKey(Beverage, on_delete = models.CASCADE, related_name="classification")
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return f"{self.id}: [type:{self.category}, name:{self.name}]"
    