import requests
import json

has = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{has}.json')
rates = json.loads(r.text)
if has == 'usd':
    cache = {'usd': 1, 'eur': rates['eur']['rate']}
elif has == 'eur':
    cache = {'usd': rates['usd']['rate'], 'eur': 1}
else:
    cache = {'usd': rates['usd']['rate'], 'eur': rates['eur']['rate']}

while True:
    wants = input().lower()
    if not wants:
        break
    amount = float(input())

    print('Checking the cache...')
    if wants in cache.keys():
        print('Oh! It is in the cache!')
        rate = cache[wants]
    else:
        print('Sorry, but it is not in the cache!')
        rate = cache[wants] = rates[wants]['rate']

    print(f'You received {round(rate * amount, 2)} {wants.upper()}.')
