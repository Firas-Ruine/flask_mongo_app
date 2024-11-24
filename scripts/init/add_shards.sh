#!/bin/bash
source ../utils/exec_in_container.sh

echo "Adding Shards to the Cluster..."
exec_in_container router01 "
    sh.addShard('rs-shard-01/shard01-a:27017,shard01-b:27017,shard01-c:27017');
    sh.addShard('rs-shard-02/shard02-a:27017,shard02-b:27017,shard02-c:27017');
"
echo "Shards added to the cluster."
