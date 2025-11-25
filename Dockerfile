FROM python:3.11-slim
WORKDIR /app

# Copy requirements first
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy full app
COPY app/ /app

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["python", "main.py"]
