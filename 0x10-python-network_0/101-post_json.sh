#!/bin/bash
# curling methods
curl -sH "Content-Type: application/json" --data @"$2" "$1"
