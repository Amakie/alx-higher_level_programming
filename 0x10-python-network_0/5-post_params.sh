#!/bin/bash
# Bash script to sent a POST request to passed URL and displays body
curl -s "$1" -d "test@gmail.com" -d "subject=I will always be here for PLD"
