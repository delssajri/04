#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

bash ${DIR}/websrv/stop.sh
bash ${DIR}/db/stop.sh

