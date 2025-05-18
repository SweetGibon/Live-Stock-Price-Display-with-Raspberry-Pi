#!/bin/bash
sleep 30  # Wait for network connection

# Set the DISPLAY environment variable for the graphical session
export DISPLAY=:0
export XAUTHORITY=/home/tapsemi/.Xauthority

# Run the stock ticker Python script
python3 /home/tapsemi/stock_ticker.py &

