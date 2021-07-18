build-image:
	docker build -t naiane/nameko-example-orders:$(TAG) .;

docker-tag:
	docker tag naiane/nameko-example-orders:$(FROM_TAG) \
	naiane/nameko-example-orders:$(TAG)

push-image:
	docker push naiane/nameko-example-orders:$(TAG)
