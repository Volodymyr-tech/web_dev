from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="supermanager",
            email="admin@example.com",
            first_name="Valdemar",
            last_name="Tesla"
        )
        admin_user.set_password("PswqPwfsqWF2212")

        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        self.stdout.write(self.style.SUCCESS(f"Администратор успешно создан: {admin_user.email}"))