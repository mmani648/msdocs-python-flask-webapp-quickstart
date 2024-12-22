# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app
RUN apt-get update && apt-get install -y poppler-utils
# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the environment variable to enable Flask's debugging
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Use gunicorn to run the Flask app (replace 'app:app' with your Flask app module)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
