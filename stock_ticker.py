import pygame
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# List of stock symbols to display
STOCK_SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META']

# Initialize Pygame
pygame.init()

# Set up the display in full-screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Stock Ticker")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 36)

def get_stock_data(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        price_element = soup.find('fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPrice'})
        price = float(price_element.text.replace(',', '')) if price_element else None
        
        change_element = soup.find('fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketChange'})
        change = float(change_element.text.replace(',', '')) if change_element else None
        
        pct_element = soup.find('fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketChangePercent'})
        pct_change = float(pct_element.text.replace('%', '').replace('(', '').replace(')', '').replace(',', '')) if pct_element else None
        
        return {
            'symbol': ticker,
            'price': price,
            'change': change,
            'percent_change': pct_change
        }
        
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def display_stocks():
    stock_info = []
    for symbol in STOCK_SYMBOLS:
        data = get_stock_data(symbol)
        if data and all([data['price'], data['change'], data['percent_change']]):
            info = f"{data['symbol']} {data['price']:.2f} {data['change']:+.2f} ({data['percent_change']:+.2f}%) <>"
            color = GREEN if data['change'] >= 0 else RED
            stock_info.append((info, color))
    return stock_info

def main():
    clock = pygame.time.Clock()
    running = True
    scroll_speed = 3
    stock_info = []
    last_update = 0
    update_interval = 90
    x = WIDTH

    while running:
        current_time = time.time()

        if not stock_info or current_time - last_update > update_interval:
            try:
                stock_info = display_stocks()
                last_update = current_time
                print("Stock info updated")
                
                ticker_widths = [font.size(text)[0] for text, _ in stock_info]
                total_ticker_width = sum(ticker_widths) + len(stock_info) * 50
            except Exception as e:
                print(f"Error updating stock info: {e}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        offset = x
        for i, ((text, color), width) in enumerate(zip(stock_info, ticker_widths)):
            text_surface = font.render(text, True, color)
            screen.blit(text_surface, (offset, HEIGHT // 2))
            offset += width + 50

        current_datetime = "Thursday, January 09, 2025, 6 PM PST"
        datetime_surface = small_font.render(current_datetime, True, WHITE)
        datetime_rect = datetime_surface.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
        screen.blit(datetime_surface, datetime_rect)

        pygame.display.flip()

        x -= scroll_speed
        if x < -(total_ticker_width - WIDTH):
            x = WIDTH

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
