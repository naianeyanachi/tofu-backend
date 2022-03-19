build-image:
	docker build -t naiane/tofu-admin-gateway:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-admin-gateway:$(FROM_TAG) \
	naiane/tofu-admin-gateway:$(TAG)

push-image:
	docker push naiane/tofu-admin-gateway:$(TAG)
