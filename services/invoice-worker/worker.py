import boto3
import json
import time
import os

# LocalStack Bağlantıları
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1', aws_access_key_id='test',
                   aws_secret_access_key='test')
s3 = boto3.client('s3', endpoint_url='http://localhost:4566', region_name='us-east-1', aws_access_key_id='test',
                  aws_secret_access_key='test')

QUEUE_URL = "http://localhost:4566/000000000000/order-processing-queue"
BUCKET_NAME = "omni-ops-invoices"


def process_invoice(order):
    order_id = order.get('order_id', 'unknown')
    # Basit bir fatura metni oluşturuyoruz (PDF simülasyonu)
    invoice_content = f"INVOICE for {order.get('customer')}\nItem: {order.get('item')}\nAmount: {order.get('amount')}"
    file_name = f"invoice_{order_id}.txt"

    # S3'e yükle
    s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=invoice_content)
    print(f" [✔] Invoice saved to S3: {file_name}")


def start_worker():
    print(" [*] Invoice Worker started. Waiting for orders...")
    while True:
        # Kuyruktan mesaj çek
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10  # Long Polling
        )

        messages = response.get('Messages', [])
        for msg in messages:
            order = json.loads(msg['Body'])
            print(f" [x] Processing order: {order.get('order_id')}")

            # İş mantığını çalıştır
            process_invoice(order)

            # İşlem bittikten sonra mesajı kuyruktan sil (Kritik!)
            sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=msg['ReceiptHandle'])
            print(f" [✔] Message deleted from queue.")


if __name__ == "__main__":
    start_worker()