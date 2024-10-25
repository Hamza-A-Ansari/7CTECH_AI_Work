#!/bin/bash

# Source the .env file to load the environment variables
source .env

echo "$(date +"%Y-%m-%d %T") Current directory: $(pwd)"

echo "Creating the build"
# Pass the environment variables to the Docker build command
 docker build --build-arg GIT_USERNAME="$GIT_USERNAME" --build-arg GIT_PASSWORD="$GIT_PASSWORD" --build-arg env="$dev" -t dev_fp-re-sys .
#  docker build --build-arg GIT_USERNAME="$GIT_USERNAME" --build-arg GIT_PASSWORD="$GIT_PASSWORD" --build-arg env="$live" -t live_fp-resys .
echo "Build is ready, running Docker"
echo "$(date +"%Y-%m-%d %T") Running the image"
 docker run dev_fp-re-sys
#  docker run live_fp-resys
