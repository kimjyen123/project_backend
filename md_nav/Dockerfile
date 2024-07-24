# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and Java (for Java-dependent libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
# openjdk-11-jdk \
# Set JAVA_HOME environment variable
# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Install pip and virtualenv
RUN pip install --upgrade pip && \
    pip install virtualenv

# Create a virtual environment
RUN virtualenv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install Cython first to ensure it's available for compiling other packages
RUN pip install --no-cache-dir Cython

# Install any needed packages specified in requirements.txt
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

# Create the staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN /app/venv/bin/python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
