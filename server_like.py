import yfinance as yf
from datetime import date, timedelta


def d_data(name):
    """Download data from Yahoo finance"""
    today = date.today()
    start = today - timedelta(days=5)

    data = yf.download(name, start=start, end=today)

    print(data)  # just for visualization

    # call the guess func
    guess_closing_price(name=name, data=None, today=today)


def guess_closing_price(name, data, today=None):
    """Guess yesterdays closing price"""

    if today is not None:
        yesterday = today - timedelta(days=1)

    #Todo Get yesterdays closing price from data 
    y_closing = 5 # placeholder

    guess = input(f'Guess yesterdays closing price for {name}: ')

    # eval guess
    if guess == y_closing:
        return 'Correct'
    elif guess > y_closing:
        return 'Too high'
    else:
        return 'Too low'

