FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip

EXPOSE 8000

CMD ["python", "task-manager.py"]