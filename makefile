LINTER = flake8
SRC_DIR = source

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
	pipenv install --dev

docs: FORCE
	cd source; make docs
