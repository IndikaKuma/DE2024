# Extending the Lab Example with Training-API

sudo docker build -t indikakuma/training-api:0.0.1 .

mkdir models  ( at the home directory)

sudo docker run -p  5002:5000 -v /home/indika_kuma/models:/usr/src/trainapp/models -d --name=training-api indikakuma/training-api:0.0.1

gcloud compute firewall-rules create flask-port-3 --allow tcp:5002

http://your_vm_ip:5002/training-api/model

# Extending the Lab Example with Training-API


sudo docker ps -a

sudo docker start prediction-ui

sudo docker start prediction-api

if there is no containers, then start them 

sudo docker run -p  5000:5000 -v /home/indika_kuma/models:/usr/src/myapp/models -d --name=prediction-api indikakumara/prediction-api:0.0.1

sudo docker run -p 5001:5000 -e PREDICTOR_API=http://prediction-api:5000/diabetes_predictor -d --name=prediction-ui indikakumara/prediction-ui:0.0.1


sudo docker network list

sudo docker network create diabetes-app-network 

sudo docker network connect diabetes-app-network prediction-api

sudo docker network connect diabetes-app-network prediction-ui

# If there is no images for prediction-api and ui

sudo docker build -t indikakumara/prediction-api:0.0.1 .

sudo docker build -t indikakumara/prediction-ui:0.0.1 .


# Check Namespace, Process IDs, etc.

sudo docker inspect --format '{{.State.Pid}}' prediction-ui | pstree -p 

sudo docker top prediction-ui

for i in $(sudo docker container ls --format "{{.ID}}"); do sudo docker inspect -f '{{.State.Pid}} {{.Name}}' $i; done

Viewing namespaces

sudo lsns 

sudo lsns --task pid

Viewing the Control Group Hierarchy

sudo apt install cgroup-tools

lscgroup 

systemd-cgls

To see a cgroup tree of the memory resource controller

systemd-cgls memory

To see a cgroup tree of docker

systemctl status docker.service

View status of a systemd service 

sudo systemctl daemon-reload

systemctl status pid | grep CGroup

Viewing Resource Controllers

cd /sys/fs/cgroup/system.slice/docker-containerID.scope

cat *

Display a live stream of container(s) resource usage statistics

sudo docker stats

# Dockerize a Node JS application

git clone https://github.com/johnpapa/node-hello.git

create the Dockerfile and then

sudo docker build -t node-hello:0.0.1 .

sudo docker run -p  5003:3000 -d --name=node-hello node-hello:0.0.1

gcloud compute firewall-rules create node-port-4 --allow tcp:5003

http://External_IP:5003/


# Containers and Port Forwarding

sudo iptables -t nat -L

 A nice article https://iximiuz.com/en/posts/docker-publish-container-ports/

# Login to a container

sudo docker exec -it prediction-ui /bin/bash

# Stop and remove all docker containers

sudo docker stop $(sudo docker ps -a -q)

sudo docker rm $(sudo docker ps -a -q)

sudo docker ps -as


# Remove all docker networks and volumes

sudo docker network prune

sudo docker volume prune

# Remove all images

sudo docker rmi -f $(sudo docker images -aq)

# Delete everything

sudo docker system prune -a --volumes
