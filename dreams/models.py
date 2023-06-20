from django.db import models


class Merchant(models.Model):
    merchant = models.CharField(max_length=100)

    def __str__(self):
        return self.merchant


class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    firm = models.CharField(max_length=100)
    model_product = models.CharField(max_length=100)
    ikpu_product = models.CharField(max_length=100)
    color_product = models.CharField(max_length=100)
    country_manufacture = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
