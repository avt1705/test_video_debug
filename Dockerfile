FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install runpod
CMD ["python", "-m", "runpod.serverless"]
