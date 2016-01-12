FROM ubuntu:latest
MAINTAINER Tatiana Drozdova <delssajri@gmail.com>
LABEL version="1.0" description="tornado basic image for pay server"
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install \
        python-tornado \
        python-couchdb && \
    apt-get clean

