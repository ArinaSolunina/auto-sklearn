FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
COPY my_script.py /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "my_script.py"]