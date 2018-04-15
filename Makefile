SHELL := /bin/bash

build:
	python3.6 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \
	cd source; \
	zip ../toast.zip toast_chest.py; \
	cd ../env/lib/python3.6/site-packages; \
	zip -g -r9 ../../../../toast.zip *;

clean:
	rm -rf env
	rm -f toast.zip