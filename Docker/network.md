### Docker Networks: CLI Management of Virtual Networks
- `docker network ls`
    - show networks
    - network bridge: default Docker virtual network, which is NAT'ed behind the HOST IP
    - network host: it gains performance by skipping virtual networks but sacrificies security of container model
- `docker network inspect <network-name>`
    - inspect the network
- `docker network create my_app_net>`
    - spawns a new virtual network for you to attach containers to 
    - it will also use the 'bridge' driver
    - network driver: built-in or 3rd party extensions that give you virtual network features


### Connect Container to the Network
- `docker container run -d --name new_nginx --network my_app_net nginx`
    - create a container with given network
- `docker network connect <network> <container>`
    - dynamically creates a NIC in a conainer on an existing virtual network
- `docker network disconnect <network> <container>`
    - removes a NIC from a container on a specific virtual network


### DNS and how Containers find each other
- Static IP's and using IP's for talking to containers is an anti-pattern. Because when you stop and restart the container, the IP may change. Do your best to avoid it.
- DNS naming is the solution. Docker uses the container names as the equivalent of a host name for containers talking to each other.
- `docker container run -d --name nginx1 --network my_app_net nginx:alpine`
- `docker container run -d --name nginx2 --network my_app_net nginx:alpine`
- `docker container exec -it nginx1 ping new nginx2`
- `docker container exec -it nginx2 ping new nginx1`
