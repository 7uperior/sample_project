# Use a more efficient Python base image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# Copy the rest of your application code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.adapters.api.main:app", "--host", "0.0.0.0", "--reload"]
