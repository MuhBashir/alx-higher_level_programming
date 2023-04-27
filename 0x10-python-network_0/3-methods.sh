#!/bin/bash
# This script display all the http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

