import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#pipenv install 'mongo[srv]' dnspython python-dotenv

MONGO_URI = os.environ.get('MONGO_URI')

