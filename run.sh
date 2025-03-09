#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: ./run_pipeline.sh <gallery_folder> <input_folder> <output_folder>"
    exit 1
fi

GALLERY_FOLDER=$1
INPUT_FOLDER=$2
OUTPUT_FOLDER=$3

#check if .env file exists
if [ ! -f .env ]; then
  touch .env
  echo "LIGHTLY_KEY=your_key" > .env
fi

# Load LIGHTLY_KEY from .env file
export LIGHTLY_KEY=$(grep LIGHTLY_KEY .env | cut -d '=' -f2)

CONTAINER_NAME="lightly_worker"

# Start the container (assuming your provided run_container.sh already has the container startup logic)
echo "Starting Lightly Docker container..."

docker run --shm-size="8196m" --rm -it \
	-v "$INPUT_FOLDER:/input_mount:ro" \
  -v "$HOME:/lightly_mount" \
	-e LIGHTLY_TOKEN="$LIGHTLY_KEY" \
	lightly/worker:latest &
# Wait briefly to ensure container is ready
sleep 10

echo "Running pipeline..."

python src/pipeline.py "$GALLERY_FOLDER" "$INPUT_FOLDER" "$OUTPUT_FOLDER"

# Optionally, stop the container after pipeline completes

echo "All done!"
