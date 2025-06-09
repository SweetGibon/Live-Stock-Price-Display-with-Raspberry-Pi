Live Stock Price Display on Raspberry Pi

This repository lets you build a real-time stock ticker display system using a Raspberry Pi board and a Raspberry Pi display. Written in Python, it uses Pygame for scrolling graphics and fetches live market data from Alpha Vantage.

Perfect for DIY finance enthusiasts, this display shows real-time price updates for any number of US-listed stocks, including symbols, current prices, and percentage changes. It’s ideal for building a home stock ticker, IoT finance display, or Raspberry Pi market dashboard.

Features

•	Real-time stock prices from Alpha Vantage API

•	Supports custom stock symbols (e.g., AAPL, GOOGL, MSFT, AMZN, META)

•	Color-coded price changes: green (up), red (down)

•	Smooth scrolling ticker using Pygame

•	Auto-refreshes data every 60 seconds

•	Configurable scrolling speed

•	Low-power mode outside market hours

•	Automatically starts at 6:15am PT and stops at 10:00am PT using crontab and bash scripts


Hardware Requirements
Before getting started, refer to the Hardware Components document to purchase the necessary parts. At a minimum, you'll need:
•	Raspberry Pi 3B+, 4, or later
•	External display (e.g., HDMI screen or Raspberry Pi Display)
•	Power supply
•	Network connection (Wi-Fi or Ethernet)

Setup Instructions
1.	Install Required Software
Follow the instructions in the System Software Setup file to install Python, Pygame, and other dependencies.
2.	Remote Access Setup
Install PuTTY for easy SSH access to your Raspberry Pi.
Follow Steps 1–2 in Program the System.
3.	Get the Stock Ticker Script
Download or copy the contents of stock_ticker.py.
Save it to your Raspberry Pi.
4.	Get Your Free Alpha Vantage API Key
Follow instructions in the Alpha Vantage API file.
Enter the API key in your stock_ticker.py file where indicated.
5.	Run the Script “python nano stock_ticker.py”

Automation (Optional)
To automatically start and stop the program during U.S. market hours (6:15 AM – 1:00 PM PT):
•	Review and install the provided crontab entries and shell scripts.
•	These will:
	Launch the script each morning
	Kill it after market close
	Put the system into low-power mode during off hours

Project Files
•	stock_ticker.py: Core Python script for the stock ticker
•	System Software Setup: Steps for configuring Raspberry Pi
•	Hardware Components: Required parts list
•	Alpha Vantage API: How to get and use your API key
•	Program the System: SSH & execution steps
•	crontab + Scripts: For automation & power management
