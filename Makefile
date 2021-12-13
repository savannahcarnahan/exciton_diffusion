
define create-env
virtualenv venv -p python3
endef

init:
	pip install -r requirements.txt

test:
	pytest

check: init
	@$(FLAKE8) src

run:
	python3 driver.py

clean:
	@rm -rf .cache
	@find . -name *.pyc -delete
	@find . -type d -name __pycache__ -delete


.PHONY: test run clean check
