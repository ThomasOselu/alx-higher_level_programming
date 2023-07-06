#!/bin/bash
# Send the POST request with the contents of the JSON file in the request body
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
