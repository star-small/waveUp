from django.shortcuts import render
from .models import Product, Category
from pathlib import Path
import csv
import os
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.

def list_to_db():
    # category, code, vendor_code, name, price, date, description, image, slug
    # Product.objects.create(**{
    #     'code': 'ef2wefweew',
    #     'vendor_code': 'Aweqfwef2A',
    #     'name': 'led',
    #     'price': 4000,
    #     'image': 'product_image/img.png'
    # })
    # if not Category.objects.filter(name=data).exists():
    pass



def read_from_csv():
    with open(BASE_DIR / "product/file.csv", newline='', encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect='excel', delimiter=';', quotechar='|'))
        model_fields = Product._meta.get_fields()[1:-1]
        for row in rows[1:]:
            field_values = dict([(model_fields[i].name, row[i]) for i in range(len(row))])
            print(field_values)

    return rows
    # os.remove(BASE_DIR/"product/file.csv")


def show_products(request):
    products = Product.objects.all()
    rows = read_from_csv() if os.path.exists(BASE_DIR/"product/file.csv") else None
    list_to_db()
    return render(request, "pages/products.html", context={"products": products})
