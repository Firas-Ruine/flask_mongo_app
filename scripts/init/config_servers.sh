#!/bin/bash
source ../utils/exec_in_container.sh

echo "Initializing Config Server Replica Set..."
exec_in_container mongodb_config1 "
    rs.initiate({
        _id: 'rs-config',
        configsvr: true,
        members: [
            { _id: 0, host: 'mongodb_config1:27017' },
            { _id: 1, host: 'mongodb_config2:27017' },
            { _id: 2, host: 'mongodb_config3:27017' }
        ]
    });
"
echo "Config Server Replica Set initialized."
