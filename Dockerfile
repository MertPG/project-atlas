FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY project_utils.py .
COPY test_project_utils.py .

CMD ["python", "main.py"]