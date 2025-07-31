FROM python:3.10-slim

# Install system packages including Tesseract and OpenCV dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the default port
EXPOSE 8080

# Start your app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
