FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install only the libraries you want to test
RUN pip install torch moviepy opencv-python numpy pillow scipy

COPY . .

CMD ["python", "-m", "runpod.serverless"]
