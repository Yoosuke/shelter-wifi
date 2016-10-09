#!/bin/sh

PORT=14080
DEV_APPSERVER=`which dev_appserver.py`
$DEV_APPSERVER --host=0.0.0.0 --port=${PORT} app.yaml 