### Docker Compose
- Why: configure relationships between containers
- Why: save our docker container run settings in easy-to-read file
- Why: create one-liner developer environment startups
- Comprised of 2 seperate but related things:
    1. YAML-formatted file that describes our slution options for containers, networks, volumes
    2. A CLI tool `docker-compose` used for local dev/test automation with those YAML files


### docker-compose CLI
- Not a production-grade tool but ideal for local development and test
- `docker-compose up`
    - setup volumes/networks and start all containers
    - `-d` for detach, running in the background
    - use `docker-compose logs` to see the logs if `-d`
- `docker-compose down`
    - stop all containers and remove containers/volumes/networks
    - use `docker-compose down -v` to also remove volume, since docker will default protect volumes from deleted
- `docker-compose ls`


### Adding Image Building to Compose file
- Compose can also build your custom images
- Will build them with `docker-compose up` if not found in cache
- Also rebuild with `docker-compose build`
- Great for complex builds that have lots of vars or build args