import os

# Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

# Директория для html
HTML_DIR = os.path.join(ROOT_DIR, "students/html_pages")

# Создание каталога для логов, если он не существует
if not os.path.exists(HTML_DIR):
    os.makedirs(HTML_DIR)