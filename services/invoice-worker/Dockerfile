FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/invoice-worker/worker.py .

# Worker bir port açmaz, sadece çalışır
CMD ["python", "worker.py"]