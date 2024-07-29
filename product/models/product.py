from django.db import models
from product.models import Category
import factory

class Product(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500, blank=True, null=True)
  price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
  #price = models.PositiveIntegerField(null=True)
  active = models.BooleanField(default=True)
  category = models.ManyToManyField(Category, blank=True)

  
  