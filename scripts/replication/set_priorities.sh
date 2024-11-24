#!/bin/bash
source ../utils/exec_in_container.sh

echo "Setting priorities for Shard 01 Replica Set..."
exec_in_container shard01-a "
    var cfg = rs.conf();
    cfg.members[0].priority = 2; // shard01-a has higher priority
    cfg.members[1].priority = 1; // shard01-b has default priority
    cfg.members[2].priority = 0; // shard01-c is hidden
    rs.reconfig(cfg);
"
echo "Priorities set for Shard 01 Replica Set."

echo "Setting priorities for Shard 02 Replica Set..."
exec_in_container shard02-a "
    var cfg = rs.conf();
    cfg.members[0].priority = 2; // shard02-a has higher priority
    cfg.members[1].priority = 1; // shard02-b has default priority
    cfg.members[2].priority = 0; // shard02-c is hidden
    rs.reconfig(cfg);
"
echo "Priorities set for Shard 02 Replica Set."
