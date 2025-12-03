# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7


# ==================================================== BASE STAGE ==================================================== #
# ----------------------------------- SET UP BASE IMAGE AND ENVIRONMENT VARIABLES ------------------------------------ #
ARG PYTHON_VERSION=3.13.5
FROM python:${PYTHON_VERSION}-slim as base

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# To set the expected timezone in the container (from Barcelona)
ENV TZ=Europe/Madrid

# ------------------------------------------- INSTALL SYSTEM DEPENDENCIES -------------------------------------------- #
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        make \
        tzdata

# Clean up apt cache to reduce image size
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set current timezone (for proper time logging)
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# ----------------------------------------------- COPY ENTRYPOINT FILE ----------------------------------------------- #
COPY docker/ /docker/
RUN chmod 755 /docker/entrypoint.sh

# ---------------------------------------------- SET WORKING DIRECTORY ----------------------------------------------- #
WORKDIR /app/app_name

# --------------------------------------------- COPY DEPENDENCY FILE(s) ---------------------------------------------- #
COPY pyproject.toml requirements.txt ./

# ------------------------------------------- INSTALL PYTHON DEPENDENCIES -------------------------------------------- #
# Download dependencies as a separate step to take advantage of Docker's caching,
# and leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------- COPY SOURCE CODE ------------------------------------------------- #
COPY src/ ./src/


# ================================================ DEVELOPMENT STAGE ================================================= #
# --------------------------------------------- SET UP DEVELOPMENT IMAGE --------------------------------------------- #
FROM base AS dev

# --------------------------------------------- COPY DEPENDENCY FILE(s) ---------------------------------------------- #
COPY requirements-dev.txt ./

# ------------------------------------------- INSTALL PYTHON DEPENDENCIES -------------------------------------------- #
# Download dependencies as a separate step to take advantage of Docker's caching,
# and leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements-dev.txt

# ---------------------------------------------- INSTALL APP AS PACKAGE ---------------------------------------------- #
RUN python -m pip install --no-cache-dir -e .


# ================================================= PRODUCTION STAGE ================================================= #
# --------------------------------------------- SET UP PRODUCTION IMAGE ---------------------------------------------- #
FROM base AS app_name

# ---------------------------------------------- INSTALL APP AS PACKAGE ---------------------------------------------- #
RUN python -m pip install --no-cache-dir .
