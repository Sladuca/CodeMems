#!/bin/sh
# ^ just for keks
SCRIPT_DIR=$(dirname $(readlink -f "$0"))
echo "$SCRIPT_DIR"
set -x
helm init
helm serve --repo-path "$SCRIPT_DIR/../charts/repo" &
helm repo add local http://localhost:8879
set +x
