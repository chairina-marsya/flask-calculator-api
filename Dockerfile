# Use official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Expose port (default Flask port)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

