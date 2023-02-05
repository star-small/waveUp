from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product, Category
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    exclude = ("date", "slug", "from_csv")


admin.site.register(Product, CustomAdmin)
admin.site.register(Category)
