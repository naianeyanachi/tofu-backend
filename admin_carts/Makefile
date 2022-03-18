build-image:
	docker build -t naiane/tofu-carts:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-carts:$(FROM_TAG) \
	naiane/tofu-carts:$(TAG)

push-image:
	docker push naiane/tofu-carts:$(TAG)
