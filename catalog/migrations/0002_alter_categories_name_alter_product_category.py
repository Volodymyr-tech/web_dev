# Generated by Django 5.1.3 on 2024-12-08 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories.html',
            name='name',
            field=models.CharField(choices=[('Иммиграция', 'Услуги по ВНЖ'), ('Бизнес', 'Бизнес услуги'), ('Недвижимость', 'Сделки с недвижимостью'), ('Налоги', 'Налогообложение')], max_length=155, primary_key=True, serialize=False, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.categories.html', verbose_name='Категория'),
        ),
    ]
