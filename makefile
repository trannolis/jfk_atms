LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements

FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	python3 -m unittest source.db

lint: FORCE
	$(LINTER) $(SRC_DIR)/*.py

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd source; make docs
