build-image:
	docker build -t naiane/tofu-gateway:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-gateway:$(FROM_TAG) \
	naiane/tofu-gateway:$(TAG)

push-image:
	docker push naiane/tofu-gateway:$(TAG)
