# Base image for the Docker container, using Python 3.12.3 as the foundation
FROM python:3.12.2

# Setting the working directory in the container to /app, where the application code will reside
WORKDIR /app

# Copying the requirements.txt file from the current directory into the container, 
# which lists the dependencies required by the application
COPY requirements.txt .

# Installing the dependencies specified in requirements.txt using pip, 
# with the --no-cache-dir flag to prevent caching of packages
RUN pip install --no-cache-dir -r requirements.txt

# Copying the current directory contents into the container, 
# which includes the application code and other necessary files
COPY . .

# Exposing port 8000 for the application to listen on, 
# allowing incoming requests to be received by the container
EXPOSE 8000

# Add uvicorn to the PATH
ENV PATH="/usr/local/bin:$PATH"

# Running the Uvicorn ASGI server with the main application, 
# listening on host 0.0.0.0 and port 8000, with auto-reload enabled 
# for development and testing purposes
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]