#!/bin/bash

script_path="/home/rex/code/headlines/stratfor.py"

if [ "$1" == "-o" ]; then
    # Open Firefox and navigate to Stratfor's main page
    firefox https://worldview.stratfor.com &>/dev/null &
else
    # Pass all arguments to the Python script
    python3 "$script_path" "$@"
fi
