import boto3
import json
import os
from flask import Flask, request, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# --- PROMETHEUS METRİKLERİ ---
# Toplam alınan sipariş sayısı
ORDER_COUNT = Counter('order_api_total_orders', 'Total number of orders received')
# Toplam hata sayısı (SQS bağlantı hataları vb.)
ORDER_ERROR = Counter('order_api_order_errors', 'Total number of failed orders')

# --- CONFIGURATION ---
# Kubernetes Köprüsü veya Localhost seçimi
AWS_ENDPOINT = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
REGION = "us-east-1"
QUEUE_NAME = "order-processing-queue"
QUEUE_URL = f"{AWS_ENDPOINT}/000000000000/{QUEUE_NAME}"

# --- AWS CLIENT ---
sqs = boto3.client(
    'sqs',
    endpoint_url=AWS_ENDPOINT,
    region_name=REGION,
    aws_access_key_id='test',
    aws_secret_access_key='test'
)


@app.route('/order', methods=['POST'])
def create_order():
    # Her istek geldiğinde sayacı artır
    ORDER_COUNT.inc()

    order_data = request.json
    if not order_data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # SQS Kuyruğuna Mesaj Gönder
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(order_data)
        )
        return jsonify({
            "status": "Order Received",
            "message_id": response.get("MessageId"),
            "target_endpoint": AWS_ENDPOINT,
            "data": order_data
        }), 202

    except Exception as e:
        # Hata durumunda hata sayacını artır (Grafana'da kırmızı çizgiyi bu çizecek!)
        ORDER_ERROR.inc()
        return jsonify({
            "error": str(e),
            "attempted_endpoint": AWS_ENDPOINT
        }), 500


# --- METRICS ENDPOINT ---
# Prometheus bu adresi (http://pod-ip:5001/metrics) kazıyacak (scrape)
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200


if __name__ == '__main__':
    # host='0.0.0.0' Kubernetes içinde erişim için zorunludur
    app.run(host='0.0.0.0', port=5001)