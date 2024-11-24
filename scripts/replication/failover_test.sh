#!/bin/bash
source ../utils/exec_in_container.sh

echo "Stopping primary node of Shard 01 (shard01-a)..."
docker stop shard01-a
sleep 10

echo "Checking the new primary of Shard 01..."
exec_in_container shard01-b "
    var status = rs.status();
    var primary = status.members.find(m => m.stateStr === 'PRIMARY');
    print('New Primary: ' + primary.name);
"

echo "Restarting the original primary node (shard01-a)..."
docker start shard01-a
sleep 10

echo "Verifying Shard 01 Replica Set status..."
exec_in_container shard01-a "
    var status = rs.status();
    var members = status.members.map(m => ({
        name: m.name,
        state: m.stateStr,
        health: m.health
    }));
    print(JSON.stringify(members, null, 2));
"