# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

COPY app /app
COPY .env .env

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3","app.py"]
