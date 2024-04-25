#!/bin/bash
# curling methods
curl -sI "$1" | grep -i allow | cut -d ' ' -f 2-
