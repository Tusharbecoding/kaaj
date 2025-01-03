FROM mcr.microsoft.com/playwright/python:v1.38.0-focal

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (Chromium, Firefox, Webkit)
RUN playwright install chromium

# Copy application code
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Start the Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
