#!/bin/bash

# --- DevOps CI/CD Pipeline Script ---
# This script automates the process of running the Flask application and the Selenium tests.
# It is designed to be executed in a CI/CD environment or locally for automated testing.

# Exit immediately if a command exits with a non-zero status.
set -e

# --- New: Activate the Python virtual environment ---
# This is crucial for the script to find the 'python' executable and
# all project dependencies (Flask, selenium, etc.).
echo "Activating Python virtual environment..."
source venv/bin/activate

# Define a function to clean up the Flask process
cleanup() {
    echo "Stopping the Flask application..."
    # Kill the Flask process using the process ID stored in FLASK_PID
    kill $FLASK_PID
    echo "Cleanup complete."
}

# Register the cleanup function to be called on script exit
# The `EXIT` trap ensures cleanup runs even if the script fails or is interrupted
trap cleanup EXIT

echo "Starting the Flask application in the background..."
# Run the Flask application in the background and capture its process ID
# The app will run on http://127.0.0.1:5000
python app.py &
FLASK_PID=$! # Store the process ID of the background Flask process

# --- Health Check Loop ---
# Wait for the Flask application to be ready before running tests.
# This is a more robust alternative to a fixed 'sleep' command.
echo "Performing a health check to wait for the Flask app to be ready..."
start_time=$(date +%s)
timeout=60
while true; do
    # Check if the server is responsive
    if curl -s http://127.0.0.1:5000 &>/dev/null; then
        echo "Flask app is ready. Proceeding with tests."
        break # Exit the loop if the health check passes
    fi

    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))

    if [ "$elapsed_time" -ge "$timeout" ]; then
        echo "Error: Flask app failed to start within $timeout seconds."
        exit 1
    fi

    # Wait for 1 second before the next check to avoid a tight loop
    sleep 1
done

echo "Running the Selenium tests with pytest..."
# Execute pytest to run all tests in the project
# Pytest will automatically discover tests in the 'tests' directory
pytest

echo "Test run completed successfully."
