# Stage 1: Clone and install dependencies
FROM ubuntu:latest as builder

# Define build arguments for Git username and password
# ARG GIT_USERNAME
# ARG GIT_PASSWORD
# ARG PORT
# # ARG env

# Set environment variables from build arguments
# ENV GIT_USERNAME=$GIT_USERNAME
# ENV GIT_PASSWORD=$GIT_PASSWORD
# ENV PORT=$PORT
# ENV ENV=$env

# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    python3.12 \
    python3-pip \
    python3-venv

# Set the working directory
WORKDIR /fp-im-rec

# Clone the Bitbucket repository with authentication
# RUN git clone --branch version2 --single-branch https://${GIT_USERNAME}:${GIT_PASSWORD}@bitbucket.org/njcodemonster/socialimagerecog.git .

# Make directory
# RUN mkdir -p all_images

# Copy necessary files from the repository
COPY Code /fp-im-rec/

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source venv/bin/activate && pip3 install -r requirements.txt"

# Expose the port (this can be made dynamic using the .env file at runtime)
EXPOSE 8080

# Set the command to run the main.py script
CMD ["bash", "-c", "source venv/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8080"]