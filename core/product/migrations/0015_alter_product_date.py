# Generated by Django 4.1.5 on 2023-01-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0014_alter_product_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
