FROM python:3.10-slim

LABEL maintainer="Mary Beck"
LABEL description="Enterprise AI Model Serving"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.serve:app", "--host", "0.0.0.0", "--port", "8000"]
