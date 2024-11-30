import os

# Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

# Директория для логов
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# Директория для html
HTML_DIR = os.path.join(ROOT_DIR, "catalog/html_pages")

# Директория для файлов с данными
DATA_DIR = os.path.join(ROOT_DIR, "data")


# Создание каталога для логов, если он не существует
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)