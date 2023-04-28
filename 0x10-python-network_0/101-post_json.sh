#!/bin/bash
# This script sends a json post request and display the response of the body
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
