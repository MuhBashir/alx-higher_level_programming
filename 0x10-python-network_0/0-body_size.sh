#!/bin/bash
# This script sends a request and display the size of the response
curl -s "$1" | wc -c
