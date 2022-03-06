build-image:
	docker build -t naiane/tofu-users:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-users:$(FROM_TAG) \
	naiane/tofu-users:$(TAG)

push-image:
	docker push naiane/tofu-users:$(TAG)
