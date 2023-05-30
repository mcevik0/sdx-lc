# AtlanticWave-SDX Local Controller Service

[![lc-ci-badge]][lc-ci] [![lc-cov-badge]][lc-cov]

## Overview

SDX Local Controller (sdx-lc) is a swagger-enabled Flask server server
based on the [swagger-codegen] project.  SDX-LC uses [connexion]
library on top of Flask.

## Running SDX Local Controller with Docker Compose

Adjust the environment in `docker-compose.yml` (these will be
eventually parameterized), and run Docker Compose from the top-level
directory:

```console
$ docker-compose up --build
```

Or, to build the image and run:

```console
$ docker build -t swagger_server .
$ docker run -p 8080:8080 swagger_server
```

## Prerequisite: run the RabbitMQ server

The communication between SDX controller and Local controller rely on
RabbitMQ. RabbitMQ can either run on the SDX controller, or run on a
separate node. The easiest way to run RabbitMQ is using docker:

```
sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:latest
```

Then in `env` and `docker-compose.yml` files, change `MQ_HOST` host to
the corresponding IP address or hostname of the RabbitMQ server

You also will need a MongoDB server:

```console
$ docker run -it --rm --name mongo \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=guest \
    -e MONGO_INITDB_ROOT_PASSWORD=guest \
    mongo:3.7
```

## Run with Python

It would be helpful to use a virtual environment:

```console
$ python3 -m venv venv
$ source venv/bin/activate
```

To run the swagger server, please execute the following from the root
directory:

```console
$ pip3 install -r requirements.txt
$ python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/SDX-LC/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/SDX-LC/1.0.0/swagger.json
```

To launch the integration tests, use tox:

```console
$ pip install tox
$ tox
```

## Communication between SDX Controller and Local Controller

The SDX controller and local controller communicate using
RabbitMQ. All the topology and connectivity related messages are sent
with RPC, with receiver confirmation. The monitoring related messages
are sent without receiver confirmation.

Below are two sample scenarios for RabbitMQ implementation:

SDX controller breaks down the topology and sends connectivity
information to local controllers:

![SDX controller to local controller][sdx-controller-to-lc]

Local controller sends domain information to SDX controller:

![Local controller to SDX controller][sdx-lc-to-controller]


<!-- URLs -->

[lc-ci-badge]: https://github.com/atlanticwave-sdx/sdx-lc/actions/workflows/test.yml/badge.svg
[lc-ci]: https://github.com/atlanticwave-sdx/sdx-lc/actions/workflows/test.yml

[lc-cov-badge]: https://coveralls.io/repos/github/atlanticwave-sdx/sdx-lc/badge.svg
[lc-cov]: https://coveralls.io/github/atlanticwave-sdx/sdx-lc

[swagger-codegen]: https://github.com/swagger-api/swagger-codegen
[connexion]: https://github.com/zalando/connexion

[sdx-controller-to-lc]: https://user-images.githubusercontent.com/29924060/139590360-d6c9aaef-e9ba-4c32-a8f9-7a0644b4b35f.jpg
[sdx-lc-to-controller]: https://user-images.githubusercontent.com/29924060/139590365-361b4f46-984c-4ab6-8d47-83c9c362910b.jpg
