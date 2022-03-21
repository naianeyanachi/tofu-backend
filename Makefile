HTMLCOV_DIR ?= htmlcov
TAG ?= dev
IMAGES := carts gateway

install-dependencies:
	pip install -U -e "carts/.[dev]"
	pip install -U -e "gateway/.[dev]"

# test

coverage-html:
	coverage html -d $(HTMLCOV_DIR) --fail-under 100

coverage-report:
	coverage report -m

test:
	flake8 carts gateway
	coverage run -m pytest gateway/test $(ARGS)
	coverage run --append -m pytest carts/test $(ARGS)

coverage: test coverage-report coverage-html

prettier:
	flake8 .

isort:
	isort --recursive .

# docker

build-base:
	docker build --target base -t nameko-example-base .;
	docker build --target builder -t nameko-example-builder .;

build: build-base
	for image in $(IMAGES) ; do TAG=$(TAG) make -C $$image build-image; done

docker-save:
	mkdir -p docker-images
	docker save -o docker-images/examples.tar $(foreach image,$(IMAGES),naiane/nameko-example-$(image):$(TAG))

docker-load:
	docker load -i docker-images/examples.tar

docker-tag:
	for image in $(IMAGES) ; do make -C $$image docker-tag; done

docker-login:
	docker login --password=$(DOCKER_PASSWORD) --username=$(DOCKER_USERNAME)

push-images:
	for image in $(IMAGES) ; do make -C $$image push-image; done
