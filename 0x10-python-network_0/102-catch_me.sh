#!/bin/bash
# curling methods
curl -s -o /dev/null '0.0.0.0:5000/catch_me' -w 'You got me!'
