FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Запускаем приложение с помощью gunicorn
CMD ["gunicorn", "taskmanager.wsgi:application", "--bind", "0.0.0.0:8000"]
