#!/bin/bash

websrv_container_name="delssajri_websrv"
couchdb_container_name="delssajri_couchdb"

echo "Stopping ${couchdb_container_name}..."
docker kill $couchdb_container_name

