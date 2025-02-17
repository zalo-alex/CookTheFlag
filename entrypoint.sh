#!/bin/bash

FLASK_DB_MIGRATION=1 flask db upgrade
gunicorn -k gevent app:app -b 0.0.0.0:8080 # TODO: USE ASYNC EVENT HANDLER