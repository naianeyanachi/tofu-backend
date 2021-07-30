build-image:
	docker build -t naiane/tofu-market-gateway:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-market-gateway:$(FROM_TAG) \
	naiane/tofu-market-gateway:$(TAG)

push-image:
	docker push naiane/tofu-market-gateway:$(TAG)
