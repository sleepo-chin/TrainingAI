FROM python:3.6.8-slim-stretch
RUN apt-get update && apt-get install -y python-pip \
    && apt-get clean
WORKDIR /app
COPY api.py .env model1.h5 requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn api:app --host 0.0.0.0 --port 80 --workers 6