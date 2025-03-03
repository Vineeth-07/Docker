# Use a smaller base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy script and data files into the container
COPY scripts/text_processor.py /app/
COPY data /home/data/

# Install dependencies (optimized)
RUN pip install --no-cache-dir requests

# Run script
CMD ["python", "/app/text_processor.py"]
