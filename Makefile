SHELL := /bin/bash

SOURCE_DIR := lambda
BUILD_DIR := dist
OUTPUT_FILE := toast_chest.zip

# Installs all production and development dependencies using pipenv
install:
	python3 -m pip install pipenv
	pipenv install --dev

# Lints all source code
lint: install
	pipenv run mypy $(SOURCE_DIR)
	pipenv run isort $(SOURCE_DIR)
	pipenv run black $(SOURCE_DIR)
	pipenv run flake8 $(SOURCE_DIR)

# Builds a production lambda-ready zip archive
build: clean-build
	pipenv run pip install -r <(pipenv lock -r) --target $(BUILD_DIR)/
	cp -r $(SOURCE_DIR) $(BUILD_DIR)/
	cd $(BUILD_DIR); zip -r ../$(OUTPUT_FILE) *

# Cleanup artifacts and build
clean-build:
	rm -rf $(BUILD_DIR)
	rm -f $(OUTPUT_FILE)

# Completely clean workspace
clean: clean-build
	pipenv --rm || true
