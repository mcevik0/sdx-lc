# AtlanticWave-SDX Local Controller Service

[![lc-ci-badge]][lc-ci] [![lc-cov-badge]][lc-cov]

## Overview

SDX Local Controller (SDX-LC) is a component of [AtlanticWave-SDX].

SDX-LC is a per-OXP (Open eXchange Point) component responsible for
interfacing the OXP network Orchestrator, or OXPO. The SDX-LC uses the
OXPO's API to submit service requests and retrieve topology data and
converts the output to the SDX data model before pushing the data to
the SDX Controller.

SDX-LC is a swagger-enabled Flask server based on the
[swagger-codegen] project, and uses [connexion] library on top of
Flask.

SDX-LC provides a REST API that other services can use.  Once SDX-LC
is up and running (see below), navigate to
http://localhost:8080/SDX-LC/1.0.0/ui/ for testing the API.  The
OpenAPI/Swagger definition should be available at
http://localhost:8080/SDX-LC/1.0.0/openapi.json.


## Requirement: RabbitMQ

The communication between SDX controller and Local controller rely on
RabbitMQ. RabbitMQ can either run on the same node as SDX controller,
or on a separate node.  The easiest way to run RabbitMQ is using
Docker:

```console
$ docker run -it --rm --name rabbitmq \
    -p 5672:5672 -p 15672:15672 \
    rabbitmq:latest
```

Then in `env` and `docker-compose.yml` files, change `MQ_HOST` host to
the corresponding IP address or hostname of the RabbitMQ server


## Running SDX Local Controller with Docker Compose

Adjust the rest of the environment in `docker-compose.yml` according
to your needs (these will be eventually parameterized), and run Docker
Compose from the top-level directory:

```console
$ docker compose up --build
```

Or, to build the image and run:

```console
$ docker build -t swagger_server .
$ docker run -p 8080:8080 swagger_server
```


## Running SDX Local Controller with Python

We will need Python 3.9.6+.  Also, in addition to RabbitMQ, we also
need a MongoDB server:

```console
$ docker run -it --rm --name mongo \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=guest \
    -e MONGO_INITDB_ROOT_PASSWORD=guest \
    mongo:3.7
```

Now create a virtual environment, install the dependencies, and run
the server:

```console
$ python3 -m venv venv --upgrade-deps
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 -m swagger_server
```


## Running tests

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

[AtlanticWave-SDX]: https://www.atlanticwave-sdx.net/

[lc-ci-badge]: https://github.com/atlanticwave-sdx/sdx-lc/actions/workflows/test.yml/badge.svg
[lc-ci]: https://github.com/atlanticwave-sdx/sdx-lc/actions/workflows/test.yml

[lc-cov-badge]: https://coveralls.io/repos/github/atlanticwave-sdx/sdx-lc/badge.svg
[lc-cov]: https://coveralls.io/github/atlanticwave-sdx/sdx-lc

[swagger-codegen]: https://github.com/swagger-api/swagger-codegen
[connexion]: https://github.com/zalando/connexion

[sdx-controller-to-lc]: https://user-images.githubusercontent.com/29924060/139590360-d6c9aaef-e9ba-4c32-a8f9-7a0644b4b35f.jpg
[sdx-lc-to-controller]: https://user-images.githubusercontent.com/29924060/139590365-361b4f46-984c-4ab6-8d47-83c9c362910b.jpg
