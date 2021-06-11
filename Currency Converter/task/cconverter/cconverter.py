import json
import requests


cache = {}
in_currency_code = input().lower()

r = requests.get(f'http://www.floatrates.com/daily/{in_currency_code}.json')
r_dict = json.loads(r.text)

if 'usd' in r_dict:
    usd_rate = r_dict['usd']['rate']
    cache['usd'] = usd_rate
if 'eur' in r_dict:
    eur_rate = r_dict['eur']['rate']
    cache['eur'] = eur_rate

while True:
    out_currency_code = input().lower()
    if out_currency_code == '':
        break
    else:
        amount = float(input())

        print('Checking the cache...')
        if out_currency_code in cache:
            print('Oh! It is in the cache!')
            money = amount * cache[f'{out_currency_code}']
            print(f'You received {money} {out_currency_code.upper()}.')
        else:
            print('Sorry, but it is not in the cache!')
            rate = r_dict[f'{out_currency_code}']['rate']
            money = amount * rate
            print(f'You received {money} {out_currency_code.upper()}.')
            cache[f'{out_currency_code}'] = rate
