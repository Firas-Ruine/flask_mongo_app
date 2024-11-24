#!/bin/bash

exec_in_container() {
  container_name=$1
  shift
  command=$@
  docker exec -it "$container_name" mongosh --eval "$command"
}
