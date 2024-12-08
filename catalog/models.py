import os
from django.db import models
from dotenv import load_dotenv
load_dotenv()
# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=155, verbose_name="Название")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(upload_to='photos/', verbose_name="Изображение", null=True, blank=True)
    category = models.ForeignKey("catalog.Categories", on_delete=models.CASCADE,
                                verbose_name="Категория",
                                related_name="products")#По умолчанию, ForeignKey связывается с первичным ключом (полем primary_key=True)
    purchase_price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
       # db_table = os.getenv("NAME")
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['purchase_price']


class Categories(models.Model):
    IMMIGRATION = "Иммиграция" #данные поля отображаются в БД
    BUSINESS = "Бизнес"
    ESTATE = "Недвижимость"
    TAXES = "Налоги"

    CATEGORIES_NAMES_CHOICES = [
        (IMMIGRATION, "Услуги по ВНЖ"),#данные поля отображаются в админке Django
        (BUSINESS, "Бизнес услуги"),
        (ESTATE, "Сделки с недвижимостью"),
        (TAXES, "Налогообложение")
    ]


    name = models.CharField(primary_key=True, max_length=155, choices=CATEGORIES_NAMES_CHOICES, verbose_name="Название категории")
    description = models.CharField(max_length=255, verbose_name="Описание категории")

    class Meta:
       # db_table = os.getenv("NAME")
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
