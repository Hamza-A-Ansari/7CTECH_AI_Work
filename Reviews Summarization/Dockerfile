# Base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive


EXPOSE 11434

# Create log directories
RUN mkdir -p /var/log/app

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3-pip \
    python3.11-venv \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -s /bin/bash appuser
WORKDIR /app

# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Copy application code
COPY --chown=appuser:appuser code /app/

# Create a virtual environment and install requirements
RUN python3.11 -m venv /app/venv && \
    /app/venv/bin/python3 -m ensurepip --upgrade && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# # Install Python packages
# RUN pip3 install --no-cache-dir -r requirements.txt

# Create a wrapper script to handle logging
RUN echo '#!/bin/bash\n\
exec python3 main.py 2>&1 | tee /var/log/app/code_run.log' > /app/start.sh && \
    chmod +x /app/start.sh

CMD ["/app/start.sh"]   