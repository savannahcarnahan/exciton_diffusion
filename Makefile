
define create-env
virtualenv venv -p python3
endef

init:
	pip install -r requirements.txt

test:
	pytest

check: test 
	@$(FLAKE8)

run: 
	python driver.py

clean:
	@rm -rf .cache
	@find . -name *.pyc -delete
	@find . -type d -name __pycache__ -delete


.PHONY: test run clean check
