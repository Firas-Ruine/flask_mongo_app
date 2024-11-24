#!/bin/bash
source ../utils/exec_in_container.sh

echo "Initializing Shard 01 Replica Set..."
exec_in_container shard01-a "
    rs.initiate({
        _id: 'rs-shard-01',
        members: [
            { _id: 0, host: 'shard01-a:27017' },
            { _id: 1, host: 'shard01-b:27017' },
            { _id: 2, host: 'shard01-c:27017' }
        ]
    });
"
echo "Shard 01 Replica Set initialized."

echo "Initializing Shard 02 Replica Set..."
exec_in_container shard02-a "
    rs.initiate({
        _id: 'rs-shard-02',
        members: [
            { _id: 0, host: 'shard02-a:27017' },
            { _id: 1, host: 'shard02-b:27017' },
            { _id: 2, host: 'shard02-c:27017' }
        ]
    });
"
echo "Shard 02 Replica Set initialized."
