#!/bin/bash

websrv_container_name="delssajri_websrv"
couchdb_container_name="delssajri_couchdb"

docker ps | grep -q "$websrv_container_name" && running="true"
if [ ! -z "$running" ] ; then
    echo "$websrv_container_name already running"
    exit
fi

docker ps -a | grep -q "$websrv_container_name" && container_exists="true"
if [ ! -z "$container_exists" ] ; then
    echo "Removing previously launched ${websrv_container_name}..."
    docker rm "$websrv_container_name"
fi

echo "Starting ${websrv_container_name}..."
docker run -d \
    -p=8888:8888 \
    --link=$couchdb_container_name:$couchdb_container_name \
    --name=$websrv_container_name \
    delssajri/payserver

