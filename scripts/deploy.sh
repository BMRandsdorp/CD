echo "Starting deployment of updated site"
# navigate to directory of active site
cd ../home
# home is in #/ updating site contents fully
# Pull contents from github
git pull origin master
# restart application
systemctl restart nginx 
# Verify the application is running
systemctl status farm

exit