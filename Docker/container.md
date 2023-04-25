### Image vs. Container
- Image
    - An image is the binaries and libraries and source code that made up your applicaion.
    - Docker's default image "registry" is called Docker Hub, it's like Github storing the source code.
- Container
    - A container is an instance of that image running as a process.
    - You can have many containers running off the same image   


### Run a Container
- `docker container run --publish 80:80 nginx`
    - what did the command do?
        1. download image 'nginx' from Docker Hub.
        2. Started a new container from that image.
        3. Opened port 80 in the host IP.
        4. Routes that traffic to the container IP, port 80.
    - use ctrl-c to stop the process when running in foreground
- `docker container run --publish 80:80 --detach nginx`
    - run in the background
- `docker container run --publish 80:80 --detach --name webhost nginx`
    - specify the container name
    - default names are random
- `docker container run --publish 80:80 -d --rm --name webhost nginx`
    - `--rm` means the container will be removed when the container ends (when you don't want to keep the container)
- `docker container ls`
    - list running containers
- `docker container ls -a`
    - list all containers


### Stop a Container
- ctrl-c
- `docker container stop <container id/name>`


### Remove a container
- `docker container rm <container-1> <container-2> ...`
    - can only remove non-running container
- `docker container rm -f <container>`
    - can remove the still running container


### Run vs. Start
- `docker container run` always starts a new container
- `docker container start` start an existing stopped one


### Logs
- `docker container logs <container name>`
    - show logs for a specific container


### Process Monitoring
- `docker container top <container>`
    - list running processes in specific container
- `docker container inspect <container>`
    - list details of one container config
- `docker container stats <container>`
    - list performance stats for all containers


### Getting a Shell Inside Containers (No Need For SSH)
#### 1. docker container run
- `docker container run -it --name proxy nginx bash`
    - `-t`: pseudo-tty
        - simulates a real terminal, like what SSH does
    - `-i`: interactive
        - keep session open to receive terminal input
    - `bash` is the [COMMAND]
    - use `exit` to exit
- `docker container run -it --name ubuntu ubuntu`
    - Its default CMD is bash, so we don't have to specify it.
- `docker container start -ai ubuntu`

#### 2. docker container exec
- `docker container exec -it mysql bash`
    - run additional process in running container