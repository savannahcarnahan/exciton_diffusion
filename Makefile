
define create-env
virtualenv venv -p python3
endef

init:
	pip install -r requirements.txt

test:
	python -m pytest

check: test 
	@$(FLAKE8)

animation:
	python -m driver $(input)

graph:
	python -m driver2 $(input)

csv:
	python -m driver3 $(input)

clean:
	@rm -rf .cache
	@find . -name *.pyc -delete
	@find . -type d -name __pycache__ -delete

doc: Makefile
	sphinx-build -M html autodoc autodoc/_build 

report: Makefile
	$(MAKE) -C report

.PHONY: test run clean check report
