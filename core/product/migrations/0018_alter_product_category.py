# Generated by Django 4.1.5 on 2023-01-26 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0017_alter_category_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.category",
            ),
            preserve_default=False,
        ),
    ]
