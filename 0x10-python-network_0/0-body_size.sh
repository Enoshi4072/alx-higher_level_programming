#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size.
curl -s "$1" | wc -c
