# pull os base image
FROM flask-base

# set work directory

WORKDIR /
RUN mkdir -p /swagger_server
COPY ./container-sdx-lc/swagger_server /swagger_server
COPY ./container-sdx-lc/curl /curl
COPY ./container-sdx-lc/curl/gunicorn.sh .
