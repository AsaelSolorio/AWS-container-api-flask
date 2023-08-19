FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add make
RUN apk add nano
RUN apk add sudo
RUN sudo apk add git build-base


WORKDIR /app_api_Flask

COPY . /app_api_Flask

EXPOSE 8080