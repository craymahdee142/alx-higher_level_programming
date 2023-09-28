#!/bin/bash
#Bash script that sends delete request to a first passed argv and displays body response
curl -sX DELETE "$1"
