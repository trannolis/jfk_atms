LINTER = flake8
SRC_DIR = source
TEST_DIR = source
NOSE_FLAGS = --with-coverage --verbose --exe --cover-package=.

FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	python -m unittest $(TEST_DIR)/test_main.py
	python3 -m "nose" ${NOSE_FLAGS}

lint: FORCE
	cd $(SRC_DIR); $(LINTER) *.py

dev_env: FORCE
	pipenv install --dev

heroku:
	# install heroku:
	curl https://cli-assets.heroku.com/install.sh | sh
	heroku login
	heroku apps:create jfk-atms
	# set up heroku app as remote for this repo
	heroku git:remote -a jfk-atms
	heroku config:set PYTHONPATH="/app"
	heroku config:set HOME="/app"

docs: FORCE
	cd source; make docs

local: FORCE
	python atms.py
