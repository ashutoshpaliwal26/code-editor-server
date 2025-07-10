# Use the official Python image
FROM python:3-alpine

# Setup the Envirtoment Variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    gcc \
    curl \
    netcat-openbsd

# Install python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Project file.
COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]