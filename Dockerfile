FROM python:alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3","app.py"]

