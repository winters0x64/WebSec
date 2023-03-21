# Docker commands

Here are some commonly used docker commands

1)docker pull image_name -> Pulls an image from the docker hub


2)docker images -> Lists all the images on the local system


3)docker ps -> Lists all the running containers


4)docker run image_name -> Starts the specific image in a container if it's not available locally it pulls the image and starts it in a container(2 commands in 1 commad)


5)docker stop container_id -> Stops a running container


6)docker start container_id -> Starts a container 


7)docker ps -a -> Lists all the running and stopped containers


8)docker build -t name_of_the_container .  -> Builds a container from the docker file in the same folder


9)docker compose up -> Similar to docker build command but a docker compose file will build and run the container with mapped ports defined in the compose file


10)docker exec -it container_id bash -> This means to execute bash inside the running docker container


11)docker image rm image_name -> This will remove  a docker image.
