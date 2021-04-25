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
