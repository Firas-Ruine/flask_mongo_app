#!/bin/bash

# Helper function for running commands inside containers
exec_in_container() {
  container=$1
  shift
  command=$@
  docker exec -it "$container" mongosh --eval "$command"
}

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

echo "Initializing Shard 1 Replica Set..."
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
echo "Shard 1 Replica Set initialized."

echo "Initializing Shard 2 Replica Set..."
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
echo "Shard 2 Replica Set initialized."

echo "Adding shards to the cluster through Router 1..."
exec_in_container mongodb_router1 "
    sh.addShard('rs-shard1/mongodb_shard1_node1:27017,mongodb_shard1_node2:27017,mongodb_shard1_node3:27017');
    sh.addShard('rs-shard2/mongodb_shard2_node1:27017,mongodb_shard2_node2:27017,mongodb_shard2_node3:27017');
"
echo "Shards added to the cluster."

exec_in_container mongodb_router1 "
    sh.status();
"
echo "MongoDB Sharded Cluster setup complete."
