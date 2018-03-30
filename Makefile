#!/usr/bin/make

install_deps:
	@virtualenv -p python3 venv
	@venv/bin/pip install -r requirements.txt
	@venv/bin/pip install -r requirements.dev.txt

flake8:
	@venv/bin/flake8 pogosnap frontend

pylint:
	@venv/bin/pylint --load-plugins pylint_django frontend pogosnap

lint: flake8 pylint
