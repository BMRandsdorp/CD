# CD assignement

The 3 main problems for continuous development were:

## 1. What do yo do to prevent a non working version of the site to be uploaded?

To make sure we won't have a CD running every time we push, we want to implement some testing.
For this we create 1 github action `Run Tests` that runs when we push to our master branch of our github repository.
This action will run pytest on the main branch to test if all pages get a 200 response code to make sure, if uploaded the page will display when it running on the live server.
And also check the content of the page.
For this pytest it will mean if new pages are added or content is changed in `main.py` that the test needs to be rewritten as well.

When the test passes the action will be completed and another github action `Update site` will run that will use the conclusion of `Run Tests` to run 1 of 2 jobs. `on-succes` job will run if `Run Tests` passed and will then start the workflow to deploy the new site and `on-failure` will return test that the pytest failed and not update anything.

## 2. How do we make sure the new files get uploaded without exposing critical info?

For this we used the github secrets to store information like:

- the SSH server's host (IP) address
- SSH private key
- Username used to connect to the server
- Password to log in to server (in case the ssh key runs into an error)
- SSH port used to connect to the SSH server

all this information can be called upon now without having to put this information inside files that could be accessed by anyone.

## 3. How do we use the stored github Secrets to connect the server?

To use these secrets in our Github action `Update Site` we run ssh-action (by appleboy) to connect to the server by using the SSH connection details inside the stored Github secrets.
SSH-action then is able to call on a script to run when the ssh connection is made. For this we ask it to run the `deploy.sh` file when connection is made.

When the script is called as part of the workflow, it will handle connecting to the server, setting up the SSH environment, and executing the script.
The script will then handle navigating to the root folder and pulling the new version of the site from the github repository.
After this the script only needs to restart the application and the new site should be live.
