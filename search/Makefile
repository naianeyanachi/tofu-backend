build-image:
	docker build -t naiane/tofu-search:$(TAG) .;

docker-tag:
	docker tag naiane/tofu-search:$(FROM_TAG) \
	naiane/tofu-search:$(TAG)

push-image:
	docker push naiane/tofu-search:$(TAG)
