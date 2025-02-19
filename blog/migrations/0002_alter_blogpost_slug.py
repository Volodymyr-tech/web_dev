# Generated by Django 5.1.3 on 2024-12-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=255, unique=True, verbose_name="Slug"
            ),
        ),
    ]
