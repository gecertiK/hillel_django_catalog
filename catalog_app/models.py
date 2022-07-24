from django.db import models


class Town(models.Model):
    town_name = models.CharField(max_length=255)

    def __str__(self):
        return self.town_name


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ManyToManyField("Product", verbose_name="product", blank=True)
    town = models.ForeignKey("Town", verbose_name="town", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.last_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name


class Retailer(models.Model):
    first_name = models.CharField(max_length=255)
    town = models.OneToOneField("Town", verbose_name="town", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
