import os

import dotenv
from django.db import models
from dotenv import load_dotenv
load_dotenv()
# Create your models here.

class Product(models.Model):

    IMMIGRATION = "immigration"
    BUSINESS = "bussines"
    TAXES = "taxes"
    REAL_ESTATE = "real_estate"

    CATEGORIES_CHOICES = [
        (IMMIGRATION, "Иммиграция"),
        (BUSINESS, "Бизнес"),
        (TAXES, "Налогообложение"),
        (REAL_ESTATE, "Недвижимость")
    ]


    name = models.CharField(max_length=155, verbose_name="Название")
    discription = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(verbose_name="Изображение")
    category = models.CharField(max_length=155, choices=CATEGORIES_CHOICES, verbose_name="Категория")
    purchase_price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.discription}'

    class Meta:
        db_table = os.getenv("NAME")
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['purchase_price']
