#!/bin/bash
# curling body size

output=$(curl -sI "$1" | grep -i "Content-Length" | awk 'print $2')

echo "$output"
