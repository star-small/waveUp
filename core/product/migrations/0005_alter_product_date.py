# Generated by Django 4.1.5 on 2023-01-25 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_product_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 25, 14, 50, 58, 697376, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
