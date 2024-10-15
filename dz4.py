import argparse

def main(number, text, verbose, repeat):
    # Выводим дополнительную информацию, если установлен флаг verbose
    if verbose:
        print("Запущен скрипт с параметрами:")
        print(f"  Число: {number}")
        print(f"  Строка: {text}")
        print(f"  Повторений: {repeat}")

    # Формируем итоговую строку с учетом параметра repeat
    output = (text + ' ') * repeat
    output = output.strip()  # Убираем лишний пробел в конце.

    # Выводим результат
    print(f"Результат: {output}")

if __name__ == "__main__":
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Обработка чисел и строк.')

    # Добавление обязательных аргументов
    parser.add_argument('number', type=int, help='Целое число')
    parser.add_argument('text', type=str, help='Строка для вывода')

    # Добавление опций
    parser.add_argument('--verbose', action='store_true', help='Выводить дополнительную информацию')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки (по умолчанию 1)')

    # Парсинг аргументов
    args = parser.parse_args()

    # Вызов основной функции с полученными аргументами
    main(args.number, args.text, args.verbose, args.repeat)
