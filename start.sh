#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

bash ${DIR}/db/start.sh || exit 1
sleep 5
bash ${DIR}/websrv/start.sh || exit 1

