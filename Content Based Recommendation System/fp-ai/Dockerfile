# Cloning Code From Bitbucket
FROM ubuntu:latest

# Define build arguments for Git username and password
ARG GIT_USERNAME
ARG GIT_PASSWORD
ARG env

# Set environment variables from build arguments
ENV GIT_USERNAME=$GIT_USERNAME
ENV GIT_PASSWORD=$GIT_PASSWORD
ENV ENV=$env
# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    python3.12 \
    python3-pip \
    python3-venv

# Set the working directory
WORKDIR /fp-re-ai-sys

# Clone the Bitbucket repository with authentication
RUN git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@bitbucket.org .

# Copy necessary files from the repository
COPY data/feature_registry/featurelist_12_1_2024_clothing.csv /fp-re-ai-sys/data/feature_registry/
COPY requirements.txt ${ENV}_config.ini /fp-re-ai-sys/

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source venv/bin/activate && pip3 install -r requirements.txt"

# Set the command to run the main.py script
CMD ["venv/bin/python3", "main.py"]
