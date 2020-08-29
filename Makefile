SHELL := /bin/bash

# Installs all production and development dependencies using pipenv
install:
	pipenv install --dev

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
