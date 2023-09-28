#!/bin/bash
#Bash script that sends a POST request to a passed url using curl
curl -s -X POST -d "email=test@gmail.com&subect=I will always be here for PLD" "$1"
