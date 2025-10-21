#!/bin/sh
set -e
mkdir -p gtfs/rt/output
# decode bundled base64 into binary pb for reproducibility
base64 -d > gtfs/rt/output/gtfs-rt-example.pb <<'BASE64'
CgUKAzIuMBITCgExGg4KBAoCVDESBgoCCHgYAg==
BASE64
echo "Wrote: gtfs/rt/output/gtfs-rt-example.pb"
ls -l gtfs/rt/output/gtfs-rt-example.pb