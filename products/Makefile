build-image:
	docker build -t naiane/nameko-example-products:$(TAG) .;

docker-tag:
	docker tag naiane/nameko-example-products:$(FROM_TAG) \
	naiane/nameko-example-products:$(TAG)

push-image:
	docker push naiane/nameko-example-products:$(TAG)
