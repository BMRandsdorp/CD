#!/bin/bash

echo "Starting deployment of updated site"

# navigate to directory of active site
cd ../home
# home is in #/ updating site contents fully
# Pull contents from github
git pull origin master
# or git pull main.py

# restart application
systemctl restart my-application
# Verify the application is running
systemctl status my-application
