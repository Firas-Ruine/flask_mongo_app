#!/bin/bash
source ../utils/exec_in_container.sh

echo "Adding Shards to the Cluster..."
exec_in_container mongodb_router1 "
    sh.addShard('rs-shard1/mongodb_shard1_node1:27017,mongodb_shard1_node2:27017,mongodb_shard1_node3:27017');
    sh.addShard('rs-shard2/mongodb_shard2_node1:27017,mongodb_shard2_node2:27017,mongodb_shard2_node3:27017');
"
echo "Shards added to the cluster."
