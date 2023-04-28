FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app

CMD [ "python", "server.py" ]
