# CD assignement

## relation github actions + secret and deploy.sh

When deploy script is called as part of a GitHub Actions workflow, the workflow will handle connecting to the server, setting up the SSH environment, and executing the script. The SSH connection details (host, username, private key, etc.) should be provided as GitHub secrets and will be accessible in the workflow.

## github action and pytest -> workflow to activate workflow
