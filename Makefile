#!/usr/bin/make

install_deps:
	@virtualenv -p python3 venv
	@venv/bin/pip install -r requirements.txt
	@venv/bin/pip install -r requirements.dev.txt
	@venv/bin/python pogosnap/manage.py migrate

flake8:
	@venv/bin/flake8 pogosnap

pylint:
	@venv/bin/pylint --load-plugins pylint_django pogosnap/frontend pogosnap/pogosnap

lint: flake8 pylint
