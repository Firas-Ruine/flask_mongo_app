#!/bin/bash
source ../utils/exec_in_container.sh

echo "Setting priorities for Shard 01 Replica Set..."
exec_in_container mongodb_shard1_node1 "
    var cfg = rs.conf();
    cfg.members[0].priority = 2; // mongodb_shard1_node1 has higher priority
    cfg.members[1].priority = 1; // mongodb_shard1_node2 has default priority
    cfg.members[2].priority = 0; // mongodb_shard1_node3 is hidden
    rs.reconfig(cfg);
"
echo "Priorities set for Shard 01 Replica Set."

echo "Setting priorities for Shard 02 Replica Set..."
exec_in_container mongodb_shard2_node1 "
    var cfg = rs.conf();
    cfg.members[0].priority = 2; // mongodb_shard2_node1 has higher priority
    cfg.members[1].priority = 1; // mongodb_shard2_node2 has default priority
    cfg.members[2].priority = 0; // mongodb_shard2_node3 is hidden
    rs.reconfig(cfg);
"
echo "Priorities set for Shard 02 Replica Set."
