# Apple Silicon (M3) uyumlu hafif imaj
FROM python:3.11-slim

WORKDIR /app

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodları kopyala
COPY services/order-api/app.py .

# Flask portunu aç
EXPOSE 5001

CMD ["python", "app.py"]