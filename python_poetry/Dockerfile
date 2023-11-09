# Use an official lightweight Python image.
FROM python:3.7.3-alpine3.9

# Install system dependencies required for building Python packages.
RUN apk update && \
    apk add --no-cache gcc musl-dev curl libffi-dev python3-dev rust cargo

# Install Poetry.
RUN pip install --upgrade pip && \
    pip install "poetry==1.1.7"

# Set Poetry to not create virtual environments.
RUN poetry config virtualenvs.create false

# Create a user and switch to it.
RUN adduser -D worker

# Set the working directory to /app.
WORKDIR /app

# Copy your 'pyproject.toml' and optionally 'poetry.lock' if present.
COPY pyproject.toml poetry.lock* /app/

# Disable the creation of virtual environments by poetry and install dependencies.
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Change the ownership of the /app directory to the worker user.
RUN chown worker:worker /app

# Copy the current directory contents into the container at /app.
COPY --chown=worker:worker . /app

# Switch to the worker user.
USER worker

# Install project dependencies using poetry.
RUN poetry install --no-dev

# Add metadata to the image to describe the maintainer and version.
LABEL maintainer="kompass_eng_0x@icloud.com" \
      version="1.0.0"

# Command to run the application when the container launches.
CMD ["python", "./src/main.py"]
