from django.core.exceptions import ValidationError


# Список запрещённых слов
FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


def validate_no_forbidden_words(value):
    '''Функция валидации формы на запрещенные слова'''
    for word in FORBIDDEN_WORDS:
        if (
            word.lower() in value.lower()
        ):  # Проверяем вхождение слова без учёта регистра
            raise ValidationError(f"Текст содержит запрещённое слово: '{word}'")
