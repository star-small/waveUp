from django.shortcuts import render
from .models import Product
from pathlib import Path
import csv
import os
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.

def read_from_csv():
    with open(BASE_DIR / "product/file.csv", newline='', encoding="utf-8-sig") as file:
        columns = csv.reader(file, dialect='excel', delimiter=';', quotechar='|')
        for data in columns:
            if data:
                try:
                    name = data[0]
                    price = int(data[1])
                    date = False if data[2] == "" else datetime.datetime.strptime(data[2], "%d.%m.%Y").date()
                    description = data[3]
                    image = "/product_image/" + data[4]

                except:
                    raise Exception("Wrong csv format")
                if date:
                    Product.objects.create(name=name, price=price,
                                           date=date,
                                           description=description,
                                           image=image)
                else:
                    Product.objects.create(name=name, price=price,
                                           description=description,
                                           image=image)
            else:
                continue
    os.remove(BASE_DIR/"product/file.csv")


def show_products(request):
    products = Product.objects.all()
    read_from_csv() if os.path.exists(BASE_DIR/"product/file.csv") else None
    for i in products:
        print(i.image)
    return render(request, "pages/products.html", context={"products": products})
