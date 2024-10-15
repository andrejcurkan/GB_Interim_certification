from datetime import datetime, timedelta


def get_future_date(days):
    # Получение текущей даты
    current_date = datetime.now()

    # Создание объекта timedelta
    future_date = current_date + timedelta(days=days)

    # Форматирование даты в нужный формат
    formatted_future_date = future_date.strftime('%Y-%m-%d')

    return formatted_future_date


# Пример использования функции
days_to_add = 10  # Количество дней для добавления
future_date = get_future_date(days_to_add)
print(f"Дата через {days_to_add} дней: {future_date}")
