from django.db import models
from django.utils.timezone import now
from decimal import Decimal
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
#wefwef

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=30, unique=True, null=False)
    vendor_code = models.CharField(
        max_length=30, unique=True, null=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=16, decimal_places=3)
    date = models.DateTimeField(default=now())
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product_image")
    slug = models.CharField(max_length=100, blank=False)
    from_csv = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f"{self.code}_on_{now().strftime('%Y-%m-%d')}"
        self.date = now() if self.date == '' else self.date

        if self.category is None:
            self.category = Category.objects.get(name="undefined")
        self.full_clean()

        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'
