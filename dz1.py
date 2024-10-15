import logging

# Настройка логгеров
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Общий уровень логирования для логгера

# Обработчик для DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log', encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)  # Логгирует DEBUG и выше

# Обработчик для WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)  # Логгирует WARNING и выше

# Форматтер для сообщений логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применение форматтера к обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логирования
logger.debug('Это сообщение уровня DEBUG.')
logger.info('Это сообщение уровня INFO.')
logger.warning('Это сообщение уровня WARNING.')
logger.error('Это сообщение уровня ERROR.')
logger.critical('Это сообщение уровня CRITICAL.')
