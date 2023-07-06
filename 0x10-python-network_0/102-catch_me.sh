#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -sL -X PUT -H "Content-Type: application/json" -d '{}' 0.0.0.0:5000/catch_me
