import os
import logging
from collections import namedtuple
import sys

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

# Настройка логирования
logging.basicConfig(
    filename='directory_contents.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def collect_directory_info(path):
    """Собирает информацию о содержимом указанной директории."""
    if not os.path.isdir(path):
        logging.error(f"Указанный путь не является директорией: {path}")
        print(f"Указанный путь не является директорией: {path}")
        return

    # Список для хранения информации о файлах и директориях
    contents = []

    # Получение списка файлов и каталогов в указанной директории
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)  # Полный путь к элементу
        parent_directory = os.path.basename(path)  # Название родительского каталога

        if os.path.isdir(full_path):
            # Если это каталог, создаем объект FileInfo с флагом is_directory = True
            info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
            contents.append(info)
            logging.info(f"Каталог: {info}")
        else:
            # Если это файл, получаем имя и расширение
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
            contents.append(info)
            logging.info(f"Файл: {info}")

    return contents

if __name__ == "__main__":
    # Проверка наличия аргументов командной строки
    if len(sys.argv) != 2:
        print("Использование: python script.py <путь_до_директории>")
        sys.exit(1)

    # Получение пути до директории из аргументов командной строки
    directory_path = sys.argv[1]
    collect_directory_info(directory_path)
