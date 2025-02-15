# Generated by Django 5.1.3 on 2025-01-24 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["id"],
                "permissions": [("can_unpublish_product", "can unpublish product")],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("not_published", "Не опубликовано"),
                    ("published", "Опубликовано"),
                ],
                default="not_published",
                max_length=15,
            ),
        ),
    ]
