build-image:
	docker build -t naiane/nameko-example-gateway:$(TAG) .;

docker-tag:
	docker tag naiane/nameko-example-gateway:$(FROM_TAG) \
	naiane/nameko-example-gateway:$(TAG)

push-image:
	docker push naiane/nameko-example-gateway:$(TAG)
