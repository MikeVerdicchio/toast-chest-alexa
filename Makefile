SHELL := /bin/bash

# Installs all production and development dependencies using pipenv
install:
	pipenv install --dev

# Lints all source code
lint: install
	pipenv run mypy source
	pipenv run isort source
	pipenv run black source
	pipenv run flake8 source

# Builds a production lambda-ready zip archive
build: clean install
	pipenv run pip install -r <(pipenv lock -r) --target dist/; \
	zip -j toast.zip source/toast_chest.py; \
	cd dist; \
	zip -g -r9 ../toast.zip *

# Cleanup directoy and builds
clean:
	pipenv --rm
	rm -rf dist
	rm -f toast.zip
