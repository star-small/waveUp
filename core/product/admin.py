from django.contrib import admin
from .models import Product, Category
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    exclude = ("date", "slug")

admin.site.register(Product, CustomAdmin)
admin.site.register(Category)
