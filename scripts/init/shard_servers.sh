#!/bin/bash
source ../utils/exec_in_container.sh

echo "Initializing Shard 01 Replica Set..."
exec_in_container mongodb_shard1_node1 "
    rs.initiate({
        _id: 'rs-shard1',
        members: [
            { _id: 0, host: 'mongodb_shard1_node1:27017' },
            { _id: 1, host: 'mongodb_shard1_node2:27017' },
            { _id: 2, host: 'mongodb_shard1_node3:27017' }
        ]
    });
"
echo "Shard 01 Replica Set initialized."

echo "Initializing Shard 02 Replica Set..."
exec_in_container mongodb_shard2_node1 "
    rs.initiate({
        _id: 'rs-shard2',
        members: [
            { _id: 0, host: 'mongodb_shard2_node1:27017' },
            { _id: 1, host: 'mongodb_shard2_node2:27017' },
            { _id: 2, host: 'mongodb_shard2_node3:27017' }
        ]
    });
"
echo "Shard 02 Replica Set initialized."
