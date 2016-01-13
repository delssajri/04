#!/bin/bash

websrv_container_name="delssajri_websrv"
couchdb_container_name="delssajri_couchdb"

echo "Stopping ${websrv_container_name}..."
docker kill $websrv_container_name

