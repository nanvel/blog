labels: Draft
created: 2017-06-06T22:57
modified: 2017-06-06T22:57
place: Phuket, Thailand
comments: true

# Docker notes

[TOC]

## Dockerfile

An example from [docs.docker.com](https://docs.docker.com/get-started/part2/#dockerfile):
```bash
# Use an official Python runtime as a base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

[Dockerfile reference](https://docs.docker.com/engine/reference/builder/) and
[Dockerfile best practices](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
on docker docs.

## Build

```bash
docker build -t <image tag> .
docker build -f Dockerfile.my  # specify dockerfile name
```

## Containers

Run (for web app):
```bash
docker run -p 4000:80 <image tag>
```

In background (detached mode):
```bash
docker run -d <image tag>
```

List containers:
```bash
docker ps  # running
docker ps -a  # all containers
```

Stop:
```bash
docker stop <container id>
docker kill <container id>  # force stop
```

Remove (from current machine):
```bash
docker rm <container id>
docker rm $(docker ps -a -q)  # remove all containers
```

## Images

List images:
```bash
docker images -a
```

Remove (from current machine):
```bash
docker rmi <image id>
docker rmi $(docker images -q)  # remove all images
```

## Networks

List networks:
```bash
docker network ls
```

Inspect:
```bash
docker network inspect <network name>
```

Create:
```
docker network create -d <driver> <network name>
```

Running containers inside a network:
```
docker run --net=my_network ...
```

## Troubleshooting

In case of failed image build, use --debug key:

```bash
image build --debug
```

sh into the image:
```bash
docker run -it <container id> bash
```

On OSX I have an error when I run shub image build for first time: Detected error connecting to Docker daemon's host.

Try this to solve it:
```bash
docker-machine restart default
eval $(docker-machine env default)
```

## AWS ECS (EC2 Container Service)

```
Cluster ->
instance ->
image ->
task definition ->
service
```

## Vocabulary

### Service

A container in production.
Codifies the way the image runs (which ports to use, how many replicas we need).

`docker-compose.yaml` example:
```yaml
version: "3"
services:
  web:
    image: username/repository:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:
```

### Swarm

A [swarm](https://docs.docker.com/get-started/part4/#understanding-swarm-clusters) is a group of machines that are running Docker and have been joined into a cluster.
