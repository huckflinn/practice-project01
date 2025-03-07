FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./data/ ./data/
COPY ./src/process_data.py ./src/process_data.py

CMD ["python3", "src/process_data.py"]