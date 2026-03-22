FROM python:3.11-slim

WORKDIR /app

COPY services/document-parser-service/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY shared/ ./shared/
COPY services/document-parser-service/ .

ENV PYTHONPATH=/app

EXPOSE 8003

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
