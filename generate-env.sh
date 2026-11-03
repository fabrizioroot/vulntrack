#!/bin/bash
# Stop immediately if a command fails so the script does not leave a partial .env file.
set -e

# Restrict this script to its owner; the executable bit remains enabled for that owner.
chmod 700 -- "$0"
# Make newly created files readable and writable only by their owner by default.
umask 077

# Create a fresh local environment file only when one does not already exist.
if [ ! -f .env ]; then
    echo ".env not found. Running the script..."
    # Generate a random Django signing key using Django's built-in helper.
    generate_key=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    # Write the key in single quotes so Compose treat special characters literally.
    printf "DJANGO_SECRET_KEY='%s'\n" "$generate_key" > .env
    # Provide a localhost default for Django's allowed-host configuration.
    echo ALLOWED_HOSTS=localhost >> .env
    # Debug mode set to True for development purposes.
    # Change value to False in production!!!
    echo DEBUG_MODE=True >> .env
else
    # Preserve the existing key instead of generating a new one on each run.
    echo ".env already exists. Skipping the script."
fi

# Enforce owner-only read/write permissions for both newly created and existing .env files.
chmod 600 -- .env
