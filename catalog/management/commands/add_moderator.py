from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Создаёт группу 'Модераторы продуктов' и назначает ей права"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модераторы продуктов")

        try:
            can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
            delete_product = Permission.objects.get(codename="delete_product")  # исправлено с config

            group.permissions.add(can_unpublish_product, delete_product)

            if created:
                self.stdout.write(self.style.SUCCESS("Группа 'Модераторы продуктов' успешно создана"))
            else:
                self.stdout.write(self.style.WARNING("Группа 'Модераторы продуктов' уже существует"))

        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))
