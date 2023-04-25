### What's In An Image (And What isn't)
    - app binaries and dependencies
    - metadata about the image data and how to run the image
    - not a complete OS, no kernel, kernel modules (e.g. drivers)


### Image Commands
- `docker image ls`
- `docker pull nginx`
- `docker pull nginx:1.11.9`
- `docker pull nginx:1.11.9-alpine`


### Images and Their Layers: Discover the Image Cache
- Images are made up of file system changes and metadata
- Each layer is uniquely identified and only stored once on a host
- This saves storage space on host and transfer time on push/pull
- A container is just a single read/write layer on top of image
- `docker image history <image-name>`
    - list image history
- `docker image inspect <image-name>`
    - returns JSON metadata about the image  


### Image Tagging and Pushinig to Docker Hub
- `docker image tag <source-image> <target-image>`
- `docker image tag nginx tony/nginx`
- `docker image tag nginx tony/nginx:latest`
    - create a tag target-image that refers to source-image
- `docker login -u ton731`
    - have to create a token first
    - enter the personal token at the password prompt after this command
- `docker image push tony/nginx`
- `docker logout`
    - if you are not on the machine you trust, remember to logout


### Building Images: Running Docker Builds
- `docker image build -t custom_nginx .`
    - in /udemy-docker-mastery/dockerfile-sample-1
    - build an image from a Dockerfile

### Extending Official Images
- `docker image build -t nginx-with-html .`
- `docker image push ton731/nginx-with-html`
    - now can push it on Docker Hub!

