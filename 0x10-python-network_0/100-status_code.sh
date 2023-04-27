#!/bin/bash
# This send a get request and display the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
