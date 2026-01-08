#!/bin/bash
set -e

echo "⏳ Waiting for Postgres..."
sleep 10

echo "Checking Hive metastore schema..."
schematool -dbType postgres -info || \
schematool -dbType postgres -initSchema

echo "Starting Hive Metastore..."
exec /opt/hive/bin/hive --service metastore
