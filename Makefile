install:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black *.py domaingen/*.py

lint:
	pylint --disable=R,C domaingen/*.py

test:
	python -m pytest -vv --cov=domaingen --cov=tests
	
debug:
	python -m pytest -vv --pdb --cov=domaingen

all: install format lint test
