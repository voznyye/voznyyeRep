import requests

url = dict(requests.get(f'http://www.floatrates.com/daily/{input().lower()}.json').json())

rate_usd, rate_eur = (url['usd']), (url['eur'])
rate_d, rate_e = (rate_usd['rate']), (rate_eur['rate'])
cache = {'usd': rate_d, 'eur': rate_e}

while True:
    convert_to = input().lower()

    if convert_to == '':
        break

    rate_name = (url[convert_to])
    rate = (rate_name['rate'])

    convert_sum = float(input())

    print('Checking the cache...')

    if convert_to in cache:
        print('Oh! It is in the cache!')
        hueta = convert_sum * cache[convert_to]
        print(f'You received {round(hueta, 2)} {convert_to.upper()}.')

    else:
        print('Sorry, but it is not in the cache!')
        hueta = convert_sum * rate
        print(f'You received {round(hueta, 2)} {convert_to.upper()}.')

        one_time_cache = {convert_to: rate}

        cache.update(one_time_cache)


