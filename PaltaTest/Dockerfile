# Dockerfile
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app/backend
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt
COPY . /app/backend