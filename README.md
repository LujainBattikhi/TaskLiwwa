# django Starterkit
A simple Django starter-kit with the basic component.

## Requirments
- Docker: https://docs.docker.com/engine/installation/
- Docker-compose: https://docs.docker.com/compose/install/

## Getting Started
1. Dlone/Download the repo:
`git clone --depth 1 https://github.com/LujainBattikhi/TaskPOSRocket`
2. navigate to django-starterkit => docker-build
`cd django-starterkit/docker-build/`
3. build docker containers
`docker-compose build`
4. Launch containers:
`docker-compose up -d`
5. Migrate DB
`docker-compose.exe exec server python manage.py migrate`
6. All done,open your browser and navigate to `http://localhost:8000/`
