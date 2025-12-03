#!/usr/bin/env sh

# ======================================================================================================================
# INCLUDES
# ======================================================================================================================
# Load logging constants and functions
. /docker/utils/logging.sh


# ======================================================================================================================
# CONSTANTS
# ======================================================================================================================
SCRIPT_PATH="$(realpath "$0")"                        # Get full path to script
PARENT_DIR="$(basename "$(dirname "$SCRIPT_PATH")")"  # Get parent directory name
SCRIPT_NAME="$(basename "$SCRIPT_PATH" .sh)"          # Get script name without extension
LOGGER_NAME="${PARENT_DIR}/${SCRIPT_NAME}"            # Combine parent and script name


# ======================================================================================================================
# LOGIC
# ======================================================================================================================
# Exit immediately if a command exits with a non-zero status
set -e

# Determine the environment
if [ "$ENV" = "prod" ]; then
  environment="production"
elif [ "$ENV" = "dev" ]; then
  environment="development"
else
  log_error "$LOGGER_NAME" "Unknown ENV (environment): $ENV"
  exit 1
fi

# Execute the appropriate command based on the first argument
log_debug "$LOGGER_NAME" "Running a command in a '$environment' environment..."
case "$1" in
  run-app_name)
    log_info "$LOGGER_NAME" "Production mode. Container is ready. Starting app..."
    exec python -m app_name.main
    ;;
  run-dev)
    log_debug "$LOGGER_NAME" "Development mode. Container is ready. Opening shell..."
    exec bash
    ;;
  *)
    log_error "$LOGGER_NAME" "Unkown command ($1). Usage: $0 {run-app_name|run-dev}"
    exit 1
    ;;
esac
