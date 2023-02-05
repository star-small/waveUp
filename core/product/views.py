from pathlib import Path
import csv
import os
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import UserForm
from django.utils.timezone import now
BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.


def dict_to_db(values_dict):
    for values in values_dict:
        category = values['category']
        values['date'] = now() if values['date'] == '' else datetime.datetime.strptime(
            values['date'], "%d %m %Y %H:%M")
        if not Category.objects.filter(name=category).exists() and category != '':
            Category.objects.create(name=category)
        values['category'] = None if category == '' else Category.objects.get(
            name=category)
        select = list(map(list, values.items()))
        select = dict(select[:5] + select[6:])
        existing_product = Product.objects.filter(
            from_csv=True, **select).first()
        print(existing_product)
        if not existing_product:
            Product.objects.create(**values, from_csv=True)


def read_from_csv():
    with open(BASE_DIR/"files/file.csv", newline='', encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect='excel',
                    delimiter=';', quotechar='|'))
        model_fields = Product._meta.get_fields()[1:-2]
        field_values = []
        for row in rows[1:]:
            field_values.append(
                dict([(model_fields[i].name, row[i]) for i in range(len(row))]))

    return field_values


def show_products(request):
    print("TEST SERVER")
    products = Product.objects.all().order_by("date")
    rows = read_from_csv() if os.path.exists(BASE_DIR/"files/file.csv") else None
    dict_to_db(rows)
    return render(request, "pages/products.html", context={"products": products})


def show_product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "pages/order.html", context={"product": product})
