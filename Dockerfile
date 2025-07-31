FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files and install Python dependencies
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port
EXPOSE 8080

# Start server
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
