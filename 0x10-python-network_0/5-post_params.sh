#!/bin/bash
# This script send a post request and display response of the body.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

