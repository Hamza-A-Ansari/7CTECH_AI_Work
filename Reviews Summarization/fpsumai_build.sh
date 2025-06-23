#!/bin/bash

# Set correct paths and directories
WORK_DIR="/home/user/ReviewSummarization/Deployment"  # Updated to correct path
LOG_DIR="$WORK_DIR/logs"
mkdir -p $LOG_DIR

# Set log file
BUILD_LOG="$LOG_DIR/docker_build.log"

# Start new build log with timestamp
echo "=== Build started at $(date) ===" > "$BUILD_LOG"
echo "Working directory: $WORK_DIR" >> "$BUILD_LOG"

# Check and stop container if running
if docker ps -q --filter "name=fpsumai" | grep -q .; then
    echo "Stopping running container..." >> "$BUILD_LOG"
    docker stop fpsumai >> "$BUILD_LOG" 2>&1
fi

# Check and remove container if exists
if docker ps -aq --filter "name=fpsumai" | grep -q .; then
    echo "Removing existing container..." >> "$BUILD_LOG"
    docker rm fpsumai >> "$BUILD_LOG" 2>&1
fi

# Check and remove image if exists
if docker images -q fpsumai | grep -q .; then
    echo "Removing existing image..." >> "$BUILD_LOG"
    docker rmi fpsumai >> "$BUILD_LOG" 2>&1
fi

# Verify and change to working directory
if [ ! -d "$WORK_DIR" ]; then
    echo "Error: Working directory $WORK_DIR does not exist" >> "$BUILD_LOG"
    echo "Available directories in /home/user/ReviewSummarization/:" >> "$BUILD_LOG"
    ls -la /home/user/ReviewSummarization/ >> "$BUILD_LOG" 2>&1
    exit 1
fi

cd "$WORK_DIR" || {
    echo "Error: Could not change to directory $WORK_DIR" >> "$BUILD_LOG"
    exit 1
}

echo "Current working directory: $(pwd)" >> "$BUILD_LOG"
echo "Directory contents:" >> "$BUILD_LOG"
ls -la >> "$BUILD_LOG"

# Check if Dockerfile exists
if [ ! -f "./Dockerfile" ]; then
    echo "Error: Dockerfile not found in $WORK_DIR" >> "$BUILD_LOG"
    echo "Directory contents:" >> "$BUILD_LOG"
    ls -la >> "$BUILD_LOG"
    exit 1
fi

# Build new image
echo "Building new fpsumai image..." >> "$BUILD_LOG"
if docker build --no-cache -t fpsumai . >> "$BUILD_LOG" 2>&1; then
    echo "fpsumai image build completed successfully at $(date)" >> "$BUILD_LOG"
    exit 0
else
    echo "Image build failed. See log for details." >> "$BUILD_LOG"
    echo "Current directory: $(pwd)" >> "$BUILD_LOG"
    echo "Directory contents:" >> "$BUILD_LOG"
    ls -la >> "$BUILD_LOG"
    exit 1
fi