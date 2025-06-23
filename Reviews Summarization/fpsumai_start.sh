# start_container.sh
#!/bin/bash

# Set paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LOG_DIR="/home/user/ReviewSummarization/Deployment/logs"
BUILD_SCRIPT="$SCRIPT_DIR/fpsumai_build.sh"

mkdir -p $LOG_DIR


# Set log file
START_LOG="$LOG_DIR/docker_run.log"

docker restart ollama
echo "ollama docker restarted at $(date) ===" > "$START_LOG"



# Initialize or clear log file
echo "=== Container start process initiated at $(date) ===" >> "$START_LOG"

# Check if image exists
if ! docker image inspect fpsumai >/dev/null 2>&1; then
    echo "fpsumai image not found. Running build script..." >> "$START_LOG"
    
    # Check if build script exists
    if [ ! -f "$BUILD_SCRIPT" ]; then
        echo "Error: Build script not found at $BUILD_SCRIPT" >> "$START_LOG"
        exit 1
    fi
    
    # Run build script and wait for it to complete
    bash "$BUILD_SCRIPT"
    BUILD_STATUS=$?
    
    # Check build status
    if [ $BUILD_STATUS -ne 0 ]; then
        echo "Failed to build image at $(date). Build script exit code: $BUILD_STATUS" >> "$START_LOG"
        exit 1
    fi
        
    echo "Image built successfully at $(date)" >> "$START_LOG"
fi

# Check if container is running and stop it
if docker ps | grep -q fpsumai; then
    echo "Found running fpsumai container. Stopping it..." >> "$START_LOG"
    docker stop fpsumai >> "$START_LOG" 2>&1
fi

# Check if container exists
if docker ps -a | grep -q fpsumai; then
    echo "Starting existing fpsumai container..." >> "$START_LOG"
    docker start fpsumai >> "$START_LOG" 2>&1
else
    echo "No existing container found. Creating and starting new container..." >> "$START_LOG"
    docker run -d \
        --gpus all \
        --name fpsumai \
	--privileged \
	-v /proc:/host_proc \
        -v /home/user/ReviewSummarization/Deployment/logs:/var/log/app \
        -v /home/user/ReviewSummarization/Deployment/code:/app/code \
        --log-driver local \
        --log-opt max-size=10m \
        --log-opt max-file=3 \
        --network="host" \
        fpsumai >> "$START_LOG" 2>&1
fi

# Verify container is running
if docker ps | grep -q fpsumai; then
    echo "Container successfully started at $(date)" >> "$START_LOG"
else
    echo "Failed to start container at $(date)" >> "$START_LOG"
fi

echo "=== Container start process completed at $(date) ===" >> "$START_LOG"
