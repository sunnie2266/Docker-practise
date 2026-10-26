# Deployment Activity 4 - Docker Starter

Use with the full step-by-step guide provided in the chat.

## Windows PowerShell commands

Starting from this folder:

```powershell
cd 01-python-app
docker build -t task4-python:v1 .
docker run --rm task4-python:v1
cd ..

cd 02-hello-web
docker build -t task4-hello-web:v1 .
docker run -d --name task4-hello-web -p 8080:5000 task4-hello-web:v1
# Open http://localhost:8080
cd ..

cd 03-study-planner
docker build -t task4-study-planner:v1 .
docker run -d --name task4-study-planner -p 8081:10000 task4-study-planner:v1
# Open http://localhost:8081 and http://localhost:8081/health
cd ..

cd 04-expense-analyser
docker build -t task4-expense:v1 .
docker run --rm task4-expense:v1
```

## Docker Hub

Replace YOUR_DOCKER_ID with your username:

```powershell
docker login
docker tag task4-study-planner:v1 YOUR_DOCKER_ID/task4-study-planner:v1
docker push YOUR_DOCKER_ID/task4-study-planner:v1
```

To verify transfer, use a genuinely different Docker host. On that other computer:

```powershell
docker pull YOUR_DOCKER_ID/task4-study-planner:v1
docker run -d --name pulled-study-planner -p 8081:10000 YOUR_DOCKER_ID/task4-study-planner:v1
```

## Public URL

Render supports image-backed web services. Create a new Web Service, choose Existing Image, enter `docker.io/YOUR_DOCKER_ID/task4-study-planner:v1`, choose a suitable compute plan (Free if available), and deploy. Confirm that its assigned public `onrender.com` URL works.

## Evidence

Use personal screenshots of account, version, hello-world output, builds, running containers, app in browser, Docker Hub upload, other Docker host pull, Render URL, and CLI program output. Do not submit sample/mock screenshots as proof of work.
