# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Команда для запуска приложения
RUN python src/main.py --prepare-db

CMD ["uvicorn", "src.main:fastapi_app", "--host", "0.0.0.0", "--port", "8000"]