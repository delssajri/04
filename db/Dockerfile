FROM ubuntu:latest
MAINTAINER Tatiana Drozdova <delssajri@gmail.com>
LABEL version="1.0" description="couchdb image for payserver"
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install couchdb && \
    apt-get clean
EXPOSE 5984
COPY ./local.ini /etc/couchdb/
VOLUME /var/run/couchdb
ENTRYPOINT ["couchdb"]

