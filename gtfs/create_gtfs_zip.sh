#!/bin/sh
set -e
mkdir -p gtfs/output
zip -j gtfs/output/gtfs_example.zip gtfs/static/*.txt
echo "Creado: gtfs/output/gtfs_example.zip"
ls -l gtfs/output/gtfs_example.zip