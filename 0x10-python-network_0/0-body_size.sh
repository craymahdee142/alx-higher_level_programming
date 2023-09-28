#!/bin/bash
#Bash script that send a request using curl and displays  the byte size of the body in response
curl -s "$1" | wc -c
