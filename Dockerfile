FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./scripts/start.sh

EXPOSE 8000

CMD ["bash", "./scripts/start.sh"]