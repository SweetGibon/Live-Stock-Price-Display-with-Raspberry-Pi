#!/bin/bash
sleep 30  # Wait for network connection

# Set the DISPLAY environment variable for the graphical session
## Replace /****/ with your username(under the home directory)
export DISPLAY=:0
export XAUTHORITY=/home/****/.Xauthority

# Run the stock ticker Python script
python3 /home/****/stock_ticker.py &

