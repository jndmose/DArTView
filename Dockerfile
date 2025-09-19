# ========================
# 1. Build frontend
# ========================
FROM node:18-alpine AS frontend-build

WORKDIR /app/client
COPY client/package*.json ./
RUN npm install
COPY client/ ./
RUN npm run build


# ========================
# 2. Backend with Flask
# ========================
FROM python:3.11-slim

WORKDIR /app

# Install system deps for numpy/pandas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend code
COPY *.py /app/
COPY static /app/static
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy built frontend into Flask's static folder
COPY --from=frontend-build /app/client/public /app/client/public

# Flask config
ENV FLASK_APP="__init__.py"
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3000

EXPOSE 3000

CMD ["flask", "run"]
