import boto3
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# LocalStack SQS Bağlantısı
sqs = boto3.client(
    'sqs',
    endpoint_url='http://localhost:4566',  # LocalStack adresi
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

QUEUE_URL = "http://localhost:4566/000000000000/order-processing-queue"


@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json

    # SQS Kuyruğuna Mesaj Gönder (Asenkron İşleme Başlangıcı)
    try:
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(order_data)
        )
        return jsonify({
            "status": "Order Received",
            "message_id": response.get("MessageId"),
            "data": order_data
        }), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)