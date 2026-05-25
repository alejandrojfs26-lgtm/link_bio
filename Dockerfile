FROM python:3.13-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv reflex

COPY . .

RUN uv pip install --system --no-cache-dir -r requirements.txt

RUN python -c "import reflex; print('Reflex OK')"

ENV PYTHONUNBUFFERED=1

STOPSIGNAL SIGKILL

EXPOSE 8000

CMD reflex run --env prod --backend-only --backend-port ${PORT:-8000}
