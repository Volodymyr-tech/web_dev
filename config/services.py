from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.apps import apps


from django.core.cache import cache
from django.apps import apps
from config.settings import CACHE_ENABLED

class CacheService:
    @staticmethod
    def get_cached_obj_or_objects(app_name: str, model_name: str, object_id=None):
        """Получает объект из кэша или базы"""
        if object_id != None and CACHE_ENABLED:

            cache_key = f"{model_name}_{object_id}"  # Генерируем ключ

        else:
            cache_key = f"{model_name}"  # Генерируем ключ для всех объектов модели

        obj = cache.get(cache_key)  # Пробуем взять объект из кэша
        if obj:
            return obj  # Если объект найден в кэше, выходим из функции


        model = apps.get_model(app_name, model_name)
        print(f"⚠️ Объекта нет в кэше, загружаем из базы...{model}")# Если объекта нет в кэше, загружаем модель

        if object_id is not None:
            obj = model.objects.get(id=object_id)
        else:
            obj = model.objects.all()  # Загружаем все объекты модели

        # Сохраняем в кэш
        if CACHE_ENABLED:
            cache.set(cache_key, obj, timeout=60 * 60)

        return obj  # Возвращаем объект
