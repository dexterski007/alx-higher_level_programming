#!/bin/bash
# curling methods
curl -s -o /dev/null -I -w "%{http_code}" "$1"
