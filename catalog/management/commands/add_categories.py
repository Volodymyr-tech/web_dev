from django.core.management.base import BaseCommand
from catalog.models import Categories
from django.core.management import call_command

class Command(BaseCommand):
    help = "Добавление продуктов в БД"

    def handle(self, *args, **options):
        Categories.objects.all().delete()

        call_command("loaddata", "fixture_categories.json")
        self.stdout.write(self.style.SUCCESS("Продукты успешно добавлены"))

