#!/bin/bash

# Helper function for running commands inside containers
exec_in_container() {
  container=$1
  shift
  command=$@
  docker exec -it "$container" mongosh --eval "$command"
}

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

echo "Adding shards to the cluster through Router 01..."
exec_in_container router01 "
    sh.addShard('rs-shard-01/shard01-a:27017,shard01-b:27017,shard01-c:27017');
    sh.addShard('rs-shard-02/shard02-a:27017,shard02-b:27017,shard02-c:27017');
"
echo "Shards added to the cluster."

exec_in_container router01 "
    sh.status();
"
echo "MongoDB Sharded Cluster setup complete."
