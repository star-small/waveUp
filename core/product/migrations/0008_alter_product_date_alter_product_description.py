# Generated by Django 4.1.5 on 2023-01-25 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_category_product_pruduct_code_product_vendor_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 25, 16, 17, 58, 28021, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
