# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Set the environment variable for SQLite database file
ENV DATABASE_URL sqlite:///./app.db

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "", "--port", "3000", "--reload"]
