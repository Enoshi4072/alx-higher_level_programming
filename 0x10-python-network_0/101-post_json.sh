#!/bin/bash
#Sends a JSON POST request to a URL passedi, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
