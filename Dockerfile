FROM python:3.11-slim

RUN apt-get update; \
    apt-get install -y --no-install-recommends build-essential libpq-dev gcc mc nano curl; \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DOCKER_RUN=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip; \
    pip install -r requirements.txt --no-cache-dir; \
    rm requirements.txt

COPY /src .