# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the requirements file into the container at /code/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . .

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
