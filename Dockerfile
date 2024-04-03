# Use a multi-stage build to include QEMU
FROM --platform=${BUILDPLATFORM:-linux/amd64} tonistiigi/binfmt:latest AS binfmt

# Build stage
FROM python:3.9 AS build

WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./app /code/app

# Final stage
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.9-slim

WORKDIR /code

# Copy QEMU binaries from the binfmt stage
COPY --from=binfmt /usr/local/bin/qemu-* /usr/local/bin/

# Copy the built application from the build stage
COPY --from=build /code /code

# Expose port 8000
EXPOSE 8000

# Set the entrypoint for the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
