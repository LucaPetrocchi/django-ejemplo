from django.contrib import admin
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=777, null=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    @admin.display(description="price range")
    def get_price_range(self):
        if self.price > 1000000:
            return "PRECIAZO ALTARRRRRRRDO BROOOOOO"
        if 500000 < self.price < 1000000:
            return "its mid lol"
        if self.price < 500000:
            return "LOL"

    def __str__(self):
        return self.name
