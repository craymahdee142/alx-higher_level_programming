#!/bin/bash
#Bash script that sends url request and displays only status code response using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
