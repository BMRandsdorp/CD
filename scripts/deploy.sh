echo "Starting deployment of updated site"

# confirm working directory
pwd 
echo "moving to home directory and print contents" 
# navigate to directory of active site
cd ..
ls

echo "run git status in directory" 
git status
# Pull contents from github
git pull origin master
# restart application
systemctl restart farm
# Verify the application is running
systemctl status farm

exit