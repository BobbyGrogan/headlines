#!/bin/bash

# Check if the script was called with the -o option
if [ "$1" == "-o" ]; then
    # Open Firefox
    firefox >/dev/null 2>&1 https://sgp.fas.org/crs/
else
    # Execute the Python script
    python3 /home/rex/code/headlines/congressionalreports.py
fi
