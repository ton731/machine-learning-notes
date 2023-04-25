### Container Lifetime & Persistent Data
- Containers are usually immutable and ephemeral. Only re-deploy containers, never change
- For the persistent data such as databases, or unique data, Docker gives us Volumes and Bind Mounts to ensure these "seperation of concerns"
- Volumes: make special location outside of container UFS (Union File System)
- Bind Mounts: link container path to host path


### Volumes
- volume will still live even the container is removed, like mysql
- `docker volume ls`
- `docker volume inspect <volume-name>`
- `docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql`
    - this will create a volume with no name (only hash)
- `docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql`
    - specify the volume name to be mysql
    - this mysql-db volume will still exist after container mysql is removed
    - next time when creating a new container, specifying mysql-db as the volume can let us get the same volume
- `docker volume create`
    - required to do this before `docker run` to use custom drivers and labels
    - most of the time we can just create volume in the `docker container run` process


### Bind Mounting
- Maps a host file or directory to a container file or directory
- Basically just two locationns pointint to the same file(s)
- Again, skip UFS, and host files overwrite any in container
- Can't use in Dockerfile specification, must be at `container run`
    - `docker container run -v /Users/tony/stuff:/path/container`
        - this works in mac/linux
- In dockerfile-sample-2/
    - `docker container run -d --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx`
        - we can see the host index.html in the nginx container now
    - `docker container rn -d --name nginx2 -p 8080:80 nginx`
        - no file in the host is shared to the container
    - `docker container exec -it nginx bash`
        - check the file inside the container