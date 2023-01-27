from django.shortcuts import render
from .models import Product, Category
from pathlib import Path
import csv
import os
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.

def dict_to_db(values_dict):
    # category, code, vendor_code, name, price, date, description, image, slug
    # Product.objects.create(**{
    #     'code': 'ef2wefweew',
    #     'category': 'efwef',
    #     'vendor_code': 'ewfwefw',
    #     'name': 'led',
    #     'price': 4000,
    #     'image': 'product_image/img.png'
    # })
    Product.objects.all().delete()
    for values in values_dict:
        category = values['category']
        values['date'] = '' if values['date'] == '' else datetime.datetime.strptime(values['date'], "%d %m %Y %H:%M")
        if not Category.objects.filter(name=category).exists() and category != '':
            Category.objects.create(name=category)
        values['category'] = None if category == '' else Category.objects.get(name=category)
        print(values)

        Product.objects.create(**values)
    #print(values)
    #if not Category.objects.filter(name=).exists():

    pass



def read_from_csv():
    with open(BASE_DIR / "product/file.csv", newline='', encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect='excel', delimiter=';', quotechar='|'))

        model_fields = Product._meta.get_fields()[1:-1]
        field_values = []
        for row in rows[1:]:
            field_values.append(dict([(model_fields[i].name, row[i]) for i in range(len(row))]))

    return field_values
    # os.remove(BASE_DIR/"product/file.csv")


def show_products(request):
    products = Product.objects.all()
    rows = read_from_csv() if os.path.exists(BASE_DIR/"product/file.csv") else None
    dict_to_db(rows)
    return render(request, "pages/products.html", context={"products": products})
