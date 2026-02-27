# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and templates
COPY src/ ./src/

# Copy trained model artifacts
COPY artifacts/ ./artifacts/

# Set working directory to src
WORKDIR /app/src

# Expose the port Flask will run on
EXPOSE 4000

# Run the Flask app
CMD ["python", "app.py"]