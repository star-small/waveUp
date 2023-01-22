from django.db import models
from django.utils.timezone import now
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=now())
    description = models.TextField()
    image = models.ImageField(upload_to="product_image")