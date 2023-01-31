from django.shortcuts import render
from .models import Product, Category
from pathlib import Path
import csv
import os
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.



def dict_to_db(values_dict):
    Product.objects.filter(from_csv=True).delete()
    for values in values_dict:
        category = values['category']
        values['date'] = '' if values['date'] == '' else datetime.datetime.strptime(values['date'], "%d %m %Y %H:%M")
        if not Category.objects.filter(name=category).exists() and category != '':
            Category.objects.create(name=category)
        values['category'] = None if category == '' else Category.objects.get(name=category)

        Product.objects.create(**values, from_csv=True)


def read_from_csv():
    with open(BASE_DIR/"files/file.csv", newline='', encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect='excel', delimiter=';', quotechar='|'))

        model_fields = Product._meta.get_fields()[1:-2]
        field_values = []
        for row in rows[1:]:
            field_values.append(dict([(model_fields[i].name, row[i]) for i in range(len(row))]))

    return field_values


def show_products(request):
    print("TEST SERVER")
    products = Product.objects.all().order_by("date")
    rows = read_from_csv() if os.path.exists(BASE_DIR/"files/file.csv") else None
    dict_to_db(rows)
    return render(request, "pages/products.html", context={"products": products})


def filter_by_price(request):
    products = Product.objects.all().order_by('-price')
    return render(request, "pages/products.html", context={"products": products})
