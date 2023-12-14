FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
COPY entities /app/entities
COPY ml /app/ml

WORKDIR /app 
RUN pip install -r requirements.txt

COPY app.py app.py

#port: 7860 pour hugging face

CMD ["uvicorn", "--host", "0.0.0.0", "app:app", "--port", "8000"]