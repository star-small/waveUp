import random

from django.db import models
from django.utils.timezone import now


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=30, default="undefined", unique=True)
    vendor_code = models.CharField(max_length=30, default="undefined", unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product_image")
    slug = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f"{self.code}_on_{now().strftime('%Y-%m-%d')}"
        self.date = now()
        if self.category == '' or self.category is None:
            self.category = Category.objects.get(name="undefined")

        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'
