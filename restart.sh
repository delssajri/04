#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

bash ${DIR}/stop.sh || exit 1
bash ${DIR}/start.sh || exit 1

