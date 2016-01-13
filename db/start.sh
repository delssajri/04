#!/bin/bash

websrv_container_name="delssajri_websrv"
couchdb_container_name="delssajri_couchdb"

docker ps | grep -q "$couchdb_container_name" && running="true"
if [ ! -z "$running" ] ; then
    echo "$couchdb_container_name already running"
    exit
fi

docker ps -a | grep -q "$couchdb_container_name" && container_exists="true"
if [ ! -z "$container_exists" ] ; then
    echo "Removing previously launched ${couchdb_container_name}..."
    docker rm "$couchdb_container_name"
fi

echo "Starting ${couchdb_container_name}..."
docker run -d \
    -p=5985:5984 \
    --hostname=couch \
    --name=$couchdb_container_name \
    delssajri/couchdb

