#!/usr/bin/env bash
set -e
docker exec -it $(docker ps -qf "name=kafka") kafka-topics --create --topic exposures --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 || true
echo "Topic 'exposures' ensured."
