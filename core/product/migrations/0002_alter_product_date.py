# Generated by Django 4.1.5 on 2023-01-25 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 25, 14, 47, 8, 864353, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
