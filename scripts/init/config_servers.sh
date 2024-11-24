#!/bin/bash
source ../utils/exec_in_container.sh

echo "Initializing Config Server Replica Set..."
exec_in_container configsvr01 "
    rs.initiate({
        _id: 'rs-config-server',
        configsvr: true,
        members: [
            { _id: 0, host: 'configsvr01:27017' },
            { _id: 1, host: 'configsvr02:27017' },
            { _id: 2, host: 'configsvr03:27017' }
        ]
    });
"
echo "Config Server Replica Set initialized."
