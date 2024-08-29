from django.db import models
from product.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )  # Adicione default=0.00
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
