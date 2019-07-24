SRS for Devs

#### Running mongo with docker locally
`docker run --name mongodb mongo:4.0.4`

#### Running our custom services with docker locally

build the container:
`docker build --rm -t <container_tag> .`

run the container and map ports:
`docker run --rm -p 8000:8000 <container_tag> >`

use `-d` if you want it to run in background

the container should now be reachable on `localhost:8000`
