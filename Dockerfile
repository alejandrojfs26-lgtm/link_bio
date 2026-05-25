FROM python:3.13-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y \
    gcc \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv reflex

COPY . .

RUN uv pip install --system --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV REFLEX_USE_UVICORN=1

STOPSIGNAL SIGKILL

EXPOSE ${PORT:-8000}

CMD reflex init && reflex run --env prod --backend-only --backend-port ${PORT:-8000}
