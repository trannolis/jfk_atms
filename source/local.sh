#!/bin/bash

# run our server locally:

mongod &
FLASK_APP=source flask run --host=127.0.0.1 --port=5000 &
mongo