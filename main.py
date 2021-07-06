import os
import requests
from datetime import date, timedelta
try:
    """Use a .env file to store API KEY"""
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
except Exception as e:
    print(e)
    quit()


def request_data(symbol: str):
    """Send the request

    Args:
        symbol (str): stock symbol

    Returns:
        dict: if request.statuscode() < 400
    """
    url_base = 'https://www.alphavantage.co/query?'
    url_functions = ['TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED']
    url_function = url_functions[0]

    url = f'{url_base}function={url_function}&symbol={symbol}&apikey={API_KEY}'

    r = requests.get(url)
    print(r.status_code)
    if r.ok:
        return r.json()
    return None


def guess_closing_price(data):
    """Guess yesterdays closing price

    Args:
        data: 

    Returns:
        str:
    """
    max_tries = 10
    tries = 0

    # Date and Time
    dt_now = date.today()
    dt_yesterday = dt_now - timedelta(days=5)

    try:
        yesterdays_closing = int(
            float(data['Time Series (Daily)'][str(dt_yesterday)]['4. close']))
    except Exception as e:
        print(e)
        print('No closing data available.')
    else:
        print(f'Yesterday: {dt_yesterday}\n')

        while tries < max_tries:
            guess = int(
                input(f'Guess yesterdays closing price: ({tries}/{max_tries}) '))
            if yesterdays_closing == guess:
                print('Correct')
                return
            elif yesterdays_closing > guess:
                tries += 1
                print('To Low')
            else:
                tries += 1
                print('To High')

        print(yesterdays_closing)


def main():

    symbol = input('Submit stock symbol (like: MSFT, IBM): ')

    data = request_data(symbol=symbol)
    if data is not None:
        guess_closing_price(data=data)


if __name__ == '__main__':
    main()
