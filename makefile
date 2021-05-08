LINTER = flake8
SRC_DIR = source
TEST_DIR = source

FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	python -m unittest $(TEST_DIR)/test_main.py 

lint: FORCE
	cd $(SRC_DIR); $(LINTER) *.py

dev_env: FORCE
	pipenv install --dev

docs: FORCE
	cd source; make docs

local: FORCE
	python atms.py
