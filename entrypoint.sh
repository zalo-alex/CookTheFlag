#!/bin/bash

flask db upgrade
gunicorn app:app -b 0.0.0.0:8080 # TODO: USE ASYNC EVENT HANDLER