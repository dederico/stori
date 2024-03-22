# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file from the root directory into the container at /app
COPY requirements.txt .

# Copy the contents of the src directory into the container at /app
COPY src/ .

# Command to run the Python script
CMD ["python", "main.py"]