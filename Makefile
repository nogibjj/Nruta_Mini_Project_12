# define the image name
IMAGE_NAME = de_mini12
DOCKER_USERNAME = nrutachoudhari

# build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# run the Docker container
run:
	docker run -p 8000:80 $(IMAGE_NAME)

# remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)

image_show:
	docker images 

container_show:
	docker ps

push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_USERNAME)/$(IMAGE_NAME)
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):latest

login:
	docker login -u ${DOCKER_USERNAME}