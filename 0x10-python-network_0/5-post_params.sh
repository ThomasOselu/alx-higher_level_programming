#!/bin/bash
# TAKES IN URL, POST AND SEND DATA
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
