# Define the Python interpreter
PYTHON := python3

# Install dependencies
install:
    $(PYTHON) -m pip install --upgrade pip
    if [ -f requirements.txt ]; then $(PYTHON) -m pip install -r requirements.txt; fi

# Start Docker services (PostgreSQL + Feddit API)
docker-start:
    docker-compose up -d

# Stop Docker services
docker-stop:
    docker-compose down

# Run tests (ensuring the database container is running first)
test:
    docker-compose up -d db  # Ensure PostgreSQL is started
    sleep 5  # Give the database time to initialize
    pytest -v test.py

# Run the Flask app (inside the container)
run:
    docker-compose up -d feddit

# Cleanup temporary files
clean:
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -delete
    rm -rf .pytest_cache

# Help command to list available targets
help:
    @echo "Available commands:"
    @echo "  make install      - Install dependencies"
    @echo "  make docker-start - Start PostgreSQL + Feddit API"
    @echo "  make docker-stop  - Stop running containers"
    @echo "  make test         - Run unit tests (ensuring PostgreSQL is up)"
    @echo "  make run          - Start the Flask application"
    @echo "  make clean        - Remove temporary files"
