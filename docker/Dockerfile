FROM python:3.9-slim-bullseye

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#COPY ../src/requirements.txt /usr/src/app/
COPY ../src/ /usr/src/app

RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
