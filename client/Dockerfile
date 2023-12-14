FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
COPY controller /app/controller
COPY pages /app/pages

WORKDIR /app 
RUN pip install -r requirements.txt

COPY accueil.py accueil.py

#port: 7860 pour hugging face

CMD ["streamlit", "run", "accueil.py", "--server.port", "8501"]