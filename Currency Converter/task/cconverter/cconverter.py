import json
import requests

YOUR_CURRENCY_CODE = input().upper()
url = f'http://www.floatrates.com/daily/{YOUR_CURRENCY_CODE}.json'
r = requests.get(url)
exchange_rates = r.json()
exchange_rates_cache = {}
if YOUR_CURRENCY_CODE != 'USD':
    exchange_rates_cache['USD'] = float(exchange_rates['usd']['rate'])
if YOUR_CURRENCY_CODE != 'EUR':
    exchange_rates_cache['EUR'] = float(exchange_rates['eur']['rate'])
while True:
    exchange_code = input().upper()
    if not exchange_code:
        break
    money_to_exchange = float(input())
    print('Checking the cache...')
    if exchange_code in exchange_rates_cache:
       print('Oh! It is in the cache!')
       currency = exchange_rates_cache[exchange_code] * money_to_exchange
    else:
        print('Sorry, but it is not in the cache!')
        exchange_rate = float(exchange_rates[exchange_code.lower()]['rate'])
        currency = exchange_rate * money_to_exchange
        exchange_rates_cache[exchange_code] = exchange_rate
    currency = "{:.2f}".format(currency)
    print(f'You received {currency} {exchange_code}.')