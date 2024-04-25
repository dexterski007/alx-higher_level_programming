#!/bin/bash
# curling methods
curl -H "Content-Type: application/json" --data @"$2" "$1"
