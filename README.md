# Stock Price Display System
This program creates a stock ticker display using a Raspberry Pi and a connected display. The software is written in Python and utilizes the Pygame library for graphics and the finance library to fetch real-time stock data.
The program displays stock information for five major tech companies: Apple, Google, Microsoft, Amazon, and Meta (formerly Facebook). It shows each stock's symbol, current price, and percentage change. The stock data is updated every 60 seconds to ensure relatively current information. You can choose any US-listed stocks and any number of stocks you want.

The display runs in full-screen mode, with the stock information scrolling from right to left across the screen. Positive price changes are shown in green, while negative changes appear in red. The scrolling speed can be adjusted by modifying the scroll_speed variable.

To start, first look at the hardware components document and purchase the necessary components.

Next, follow the instructions in the file "System Software Setup". 

Since you will be logging in to the system multiple times, it is better to download and install Putty. Once installed, follow the prompts in the file "Program the System", Steps 1 - 2. Now you need to have the "stock_ticker.py" file. You can download the file, open it in the text / document viewer in your computer and copy the content. Next from the command window connected to the Raspberry Pi, execute Step 3. 

Now you also need to have a free API Key from Alpha Vantage that you need to enter in the stock_ticker.py file. Please open up the file "Alpha Vantage API" file and follow the instructions. Once you receive the key, enter it in the appropriate line in the stock_ticker.py file. 

If you have done everything correctly, you can run "python nano stock_ticker.py". Good Luck.

Also, there are a few additional files. We wanted the program to launch automatically at 6:15am PT and be killed at 10:00am PT. The system should stay in low-power mode during the time it is not running. This was done by executing a few additional programs / bash scripts, controlled by crontab. The crontab file contents clearly explain the process.
