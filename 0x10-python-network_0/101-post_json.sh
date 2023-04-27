#!/bin/bash
# This script sends a JSON post requst and dusplay the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

