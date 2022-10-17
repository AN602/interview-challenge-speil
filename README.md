# interview-challenge-speil

### Prerequisites
* Python 3.6
* Node 16.18

### Installing project dependencies
* Run `pip install -r requirements.txt` in root folder
* Run `npm install ci` in `ui` folder

### How to run
* Run `python server.py` in root folder
* Run `npm run dev` in `ui` 
* Go to `http://localhost:5173` to access the application

### How to deploy
Deployment requires a user account on the public [docker hub](https://hub.docker.com) and [heroku](https://dashboard.heroku.com/apps).
The deployment works by building a docker image locally and pushing it to the docker hub via the heroku CLI. Then the pushed image can be linked to a heroku app and released.

Heroku CLI commands:
* `heroku container:push web -a interview-challenge-speil` -> build and push the image
* `heroku container:release web -a interview-challenge-speil` -> release and deploy the image


## Not covered topics for production readiness
* API input validation on the backend
* User input validation on the frontend
* Queuing system for classification work
* Usage of a proper web server to replace the Flask dev one
* Either usage management of rate limiting to prevent DDOSing of the API