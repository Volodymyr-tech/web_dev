from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Создаёт группу 'Контент менеджеры' и назначает ей права"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Контент-менеджер")

        try:
            add_product = Permission.objects.get(codename="add_product")
            delete_product = Permission.objects.get(codename="delete_product")
            change_product = Permission.objects.get(codename="change_product")


            group.permissions.add(add_product, delete_product, change_product)

            if created:
                self.stdout.write(self.style.SUCCESS("Группа 'Контент менеджеры' успешно создана"))
            else:
                self.stdout.write(self.style.WARNING("Группа 'Контент менеджеры' уже существует"))

        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))
