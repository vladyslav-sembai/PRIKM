# Вибираємо базовий образ
FROM python:3.10-slim

# Встановлюємо залежності
RUN pip install --no-cache-dir python-telegram-bot requests

# Копіюємо файли бота в контейнер
COPY . /app
WORKDIR /app

# Вказуємо команду для запуску бота
CMD ["python", "botcode.py"]
