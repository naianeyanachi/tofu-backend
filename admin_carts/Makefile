build-image:
	docker build -t naiane/tofu-admin-carts:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-admin-carts:$(FROM_TAG) \
	naiane/tofu-admin-carts:$(TAG)

push-image:
	docker push naiane/tofu-admin-carts:$(TAG)
