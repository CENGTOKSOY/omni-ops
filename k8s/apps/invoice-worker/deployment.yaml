apiVersion: apps/v1
kind: Deployment
metadata:
  name: invoice-worker
spec:
  replicas: 1
  selector:
    matchLabels:
      app: invoice-worker
  template:
    metadata:
      labels:
        app: invoice-worker
    spec:
      containers:
      - name: invoice-worker
        image: omni-ops-invoice-worker:v1
        imagePullPolicy: Never
        env:
        - name: AWS_ENDPOINT_URL
          value: "http://localstack-svc:4566"