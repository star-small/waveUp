from ..models import Product, Category
import datetime
from pathlib import Path
import csv
from django.utils.timezone import now
from django.urls import resolve
from django.shortcuts import render, redirect

from ..senders import AllSender

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # /home/user/..../files/


class PageRendererMixin:
    model = None
    obj = None

    def get(self, request):
        url = resolve(request.path_info).url_name  # url name from urlpattern
        obj = self.model.objects.all() if not self.obj else self.obj
        return render(
            request,
            "pages/" + url.rstrip("_url") + ".html",
            context={self.model.__name__.lower() + "s": obj},
        )

    def post(self, request):
        sender = AllSender(request.POST)
        sender.send()
        return redirect(resolve(request.path_info).url_name)


def dict_to_db(values_dict):
    for values in values_dict:
        if Product.objects.filter(vendor_code=values["vendor_code"]).exists():
            continue

        # Validation
        category = values["category"]
        values["date"] = (
            now()
            if values["date"] == ""
            else datetime.datetime.strptime(values["date"], "%d %m %Y %H:%M")
        )
        values["price_without_discount"] = (
            0
            if values["price_without_discount"] == ""
            else values["price_without_discount"]
        )
        if not Category.objects.filter(name=category).exists() and category != "":
            Category.objects.create(name=category)
        values["category"] = (
            None if category == "" else Category.objects.get(name=category)
        )

        Product.objects.create(**values)


def read_from_csv():
    with open(BASE_DIR / "files/file.csv", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect="excel", delimiter=";", quotechar="|"))
        model_fields = Product._meta.get_fields()[1:-1]
        field_values = []
        for row in rows[1:]:
            field_values.append(
                dict([(model_fields[i].name, row[i]) for i in range(len(row))])
            )
    return field_values
