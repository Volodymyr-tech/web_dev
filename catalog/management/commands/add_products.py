from django.core.management.base import BaseCommand
from catalog.models import Product,Categories
from django.core.management import call_command

class Command(BaseCommand):
    help = "Добавление продуктов в БД"

    def handle(self, *args, **options):
        Product.objects.all().delete()

        call_command("loaddata", "fixture_products.json")
        self.stdout.write(self.style.SUCCESS("Продукты успешно добавлены"))

