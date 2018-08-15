# import config.
# You can change the default config with `make cnf="config_special.env" build`
cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

CID_FILE=ncclient.cid

.PHONY: build-container run exec-test clean
.DEFAULT_GOAL := up

define docker-container =
$$(cat $(CID_FILE))
endef


# HELP
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[^_][a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build-container: ## BUILD TEST CONTAINER
	@echo 'building container $(DOCKER_IMAGE_NAME)' 
	@docker build -t $(DOCKER_IMAGE_NAME) .

run: ## RUN TEST CONTAINER
	@echo 'run docker container $(DOCKER_IMAGE_NAME)'
	@docker run --cidfile="$(CID_FILE)" --rm -i -d $(DOCKER_IMAGE_NAME)


exec-test: ## RUN TEST
	docker exec $(docker-container) nosetests test --rednose --verbosity=3 --exclude=transport --with-coverage --cover-package ncclient

clean:
	@test -f  $(CID_FILE) && { docker rm -f $(docker-container); rm $(CID_FILE); } || true;

up: build-container clean run exec-test
