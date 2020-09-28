#
#   Copyright 2015  Xebia Nederland B.V.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

# REGISTRY_HOST=docker.io
USERNAME=arya
NAME=$(shell basename $(CURDIR))

RELEASE_SUPPORT := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))/.make-release-support
API_IMAGE := $(USERNAME)/$(NAME)-api
WORKER_IMAGE := $(USERNAME)/$(NAME)-worker

VERSION = $(shell . $(RELEASE_SUPPORT) ; getVersion)
TAG = $(shell . $(RELEASE_SUPPORT); getTag)

SHELL = /bin/bash

DOCKER_BUILD_CONTEXT=.
DOCKER_FILE_PATH=Dockerfile

.PHONY: pre-build docker-build post-build build clean release patch-release minor-release major-release tag check-status check-release showver

default: build up

build: pre-build docker-build post-build

pre-build: .release


post-build: clean


api-build:
	docker build $(DOCKER_BUILD_ARGS) --target api-development -t $(API_IMAGE):$(VERSION) $(DOCKER_BUILD_CONTEXT) -f $(DOCKER_FILE_PATH)

worker-build:
	docker build $(DOCKER_BUILD_ARGS) --target worker-development -t $(WORKER_IMAGE):$(VERSION) $(DOCKER_BUILD_CONTEXT) -f $(DOCKER_FILE_PATH)

clean:
	docker rmi $(shell docker images -f "dangling=true" -q)


docker-build: api-build worker-build	
	@DOCKER_MAJOR=$(shell docker -v | sed -e 's/.*version //' -e 's/,.*//' | cut -d\. -f1) ; \
	DOCKER_MINOR=$(shell docker -v | sed -e 's/.*version //' -e 's/,.*//' | cut -d\. -f2) ; \
	if [ $$DOCKER_MAJOR -eq 1 ] && [ $$DOCKER_MINOR -lt 10 ] ; then \
		echo docker tag -f $(API_IMAGE):$(VERSION) $(API_IMAGE):latest ;\
		echo docker tag -f $(WORKER_IMAGE):$(VERSION) $(WORKER_IMAGE):latest ;\
		docker tag -f $(API_IMAGE):$(VERSION) $(API_IMAGE):latest ;\
		docker tag -f $(WORKER_IMAGE):$(VERSION) $(WORKER_IMAGE):latest ;\
	else \
		echo docker tag $(API_IMAGE):$(VERSION) $(API_IMAGE):latest ;\
		echo docker tag $(WORKER_IMAGE):$(VERSION) $(WORKER_IMAGE):latest ;\
		docker tag $(API_IMAGE):$(VERSION) $(API_IMAGE):latest ;\
		docker tag $(WORKER_IMAGE):$(VERSION) $(WORKER_IMAGE):latest ;\
	fi

.release:
	@echo "release=0.0.0" > .release
	@echo "tag=$(NAME)-0.0.0" >> .release
	@echo INFO: .release created
	@cat .release


release: check-status check-release build

snapshot: build

showver: .release
	@. $(RELEASE_SUPPORT); getVersion

tag-patch-release: VERSION := $(shell . $(RELEASE_SUPPORT); nextPatchLevel)
tag-patch-release: .release tag 

tag-minor-release: VERSION := $(shell . $(RELEASE_SUPPORT); nextMinorLevel)
tag-minor-release: .release tag 

tag-major-release: VERSION := $(shell . $(RELEASE_SUPPORT); nextMajorLevel)
tag-major-release: .release tag 

patch-release: tag-patch-release release
	@echo $(VERSION)

minor-release: tag-minor-release release
	@echo $(VERSION)makefile lazy evaluationR: tag $(TAG) for version $(VERSION) already tagged in git" >&2 && exit 1) ;
	@. $(RELEASE_SUPPORT) ; setRelease $(VERSION)
	git add .
	git commit -m "bumped to version $(VERSION)" ;
	git tag $(TAG) ;

check-status:
	@. $(RELEASE_SUPPORT) ; ! hasChanges || (echo "ERROR: there are still outstanding changes" >&2 && exit 1) ;

check-release: .release
	@. $(RELEASE_SUPPORT) ; tagExists $(TAG) || (echo "ERROR: version not yet tagged in git. make [minor,major,patch]-release." >&2 && exit 1) ;
	@. $(RELEASE_SUPPORT) ; ! differsFromRelease $(TAG) || (echo "ERROR: current directory differs from tagged $(TAG). make [minor,major,patch]-release." ; exit 1)

up:
	docker-compose up

daemon:
	docker-compose up -d

down:
	docker-compose down
