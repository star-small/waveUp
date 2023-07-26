from ..models import Product, Category
import datetime
from pathlib import Path
import csv
from django.utils.timezone import now

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # /home/user/..../files/


def dict_to_db(values_dict):
    for values in values_dict:
        category = values["category"]
        values["date"] = (
            now()
            if values["date"] == ""
            else datetime.datetime.strptime(values["date"], "%d %m %Y %H:%M")
        )
        if not Category.objects.filter(name=category).exists() and category != "":
            Category.objects.create(name=category)
        values["category"] = (
            None if category == "" else Category.objects.get(name=category)
        )
        select = list(map(list, values.items()))
        select = dict(select[:5] + select[6:])
        existing_product = Product.objects.filter(from_csv=True, **select).first()
        if not existing_product:
            Product.objects.create(**values, from_csv=True)


def read_from_csv():
    with open(BASE_DIR / "files/file.csv", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.reader(file, dialect="excel", delimiter=";", quotechar="|"))
        model_fields = Product._meta.get_fields()[1:-2]
        field_values = []
        for row in rows[1:]:
            field_values.append(
                dict([(model_fields[i].name, row[i]) for i in range(len(row))])
            )

    return field_values
