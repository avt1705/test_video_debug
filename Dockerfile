FROM python:3.10-slim

WORKDIR /app

# Install RunPod SDK
RUN pip install --no-cache-dir runpod

# Copy your handler.py into the container
COPY . .

# Run handler.py directly
CMD ["python", "handler.py"]
