LINTER = flake8
SRC_DIR = source
TEST_DIR = tests

FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	python -m unittest $(TEST_DIR)/test_endpoints.py 

lint: FORCE
	$(LINTER) $(SRC_DIR)/main.py

dev_env: FORCE
	pipenv install --dev

docs: FORCE
	python -m pydoc -b

local: FORCE
	source/local.sh