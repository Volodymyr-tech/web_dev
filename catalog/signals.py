from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from catalog.models import Product
from users.models import CustomUser


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def clear_mailing_cache(sender, instance, **kwargs):
    # Очищаем кэш для списка продуктов зарегистрированых и не зарегистрированых юзеров
    cache.delete("Product_list_Guest_non_registered_user")

    # ❗ Удаляем кэш списка для каждого user_id
    for user_id in CustomUser.objects.values_list("id", flat=True):
            cache.delete(f"Product_list_{user_id}")

    print("🚀 Кэш полностью очищен!")