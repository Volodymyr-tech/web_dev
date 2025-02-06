from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from catalog.models import Product
from users.models import CustomUser


from django.contrib.sessions.models import Session

def get_active_sessions():
    """Получает все session_id зарегистрированных пользователей"""
    sessions = Session.objects.values_list("session_key", flat=True)  # Получаем все session_id
    return sessions



@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def clear_mailing_cache(sender, instance, **kwargs):
    # Очищаем кэш для списка продуктов зарегистрированых и не зарегистрированых юзеров
    cache.delete("Product_list_Guest_non_registered_user")

    # ❗ Получаем все session_id активных пользователей
    active_sessions = get_active_sessions()

    # ❗ Удаляем кэш списка для каждого user_id + session_id
    for user_id in CustomUser.objects.values_list("id", flat=True):
        for session_id in active_sessions:
            cache.delete(f"Product_list_{user_id}_{session_id}")

    print("🚀 Кэш полностью очищен!")