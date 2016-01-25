#!/bin/bash

websrv_container_name="delssajri_websrv"
couchdb_container_name="delssajri_couchdb"

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo "Stopping ${couchdb_container_name}..."
docker kill $couchdb_container_name

