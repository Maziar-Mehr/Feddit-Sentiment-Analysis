# Use official Python image as the base
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API port
EXPOSE 8080

# Define the command to run the API
CMD ["python", "main.py"]
