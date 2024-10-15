from datetime import datetime

# Создаём словарь для перевода дней недели
days_of_week = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}

# Получение текущего времени и даты
now = datetime.now()

# Форматирование даты и времени
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Получение названия дня недели на английском и перевод на русский
day_of_week_en = now.strftime('%A')
day_of_week_ru = days_of_week.get(day_of_week_en, day_of_week_en)

# Получение номера недели в году
week_number = now.isocalendar()[1]

# Вывод результатов
print(f"Текущая дата и время: {formatted_date_time}")
print(f"День недели: {day_of_week_ru}")
print(f"Номер недели в году: {week_number}")
