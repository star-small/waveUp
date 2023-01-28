# Generated by Django 4.1.5 on 2023-01-28 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0022_alter_product_code_alter_product_vendor_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="from_csv",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 28, 8, 22, 48, 347967, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
