#!/bin/sh
# ^ just for keks
SCRIPT_DIR=$(dirname $(readlink -f "$0"))
echo "$SCRIPT_DIR"
set -x
helm init --override spec.selector.matchLabels.'name'='tiller',spec.selector.matchLabels.'app'='helm' --output yaml | sed 's@apiVersion: extensions/v1beta1@apiVersion: apps/v1@' | kubectl apply -f -
helm serve --repo-path "$SCRIPT_DIR/../charts/repo" &
helm repo add local http://localhost:8879
set +x
