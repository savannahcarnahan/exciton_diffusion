
define create-env
virtualenv venv -p python3
endef

init:
	pip install -r requirements.txt

test:
	python -m pytest

check: init
	@$(FLAKE8) src

run: init test
	python driver.py

clean:
	@rm -rf .cache
	@find . -name *.pyc -delete
	@find . -type d -name __pycache__ -delete

doc: Makefile
	sphinx-build -M html autodoc autodoc/_build 

.PHONY: test run clean check
