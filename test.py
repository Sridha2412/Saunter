__author__ = 'Sridha'

import requests, json

api_url = 'https://api.covid19api.com/'


countries = requests.get(api_url+'summary').json()


lines = sorted(countries['Countries'], key = lambda k: k.get('NewConfirmed', 0), reverse=False)

print(countries['Global'])

i = 0
for line in lines:
    # print(line)
    print(line['Country'], line['NewConfirmed'])
    i += 1
    if (i > 10):
        break

# {'Country': 'Afghanistan', 'CountryCode': 'AF', 'Slug': 'afghanistan', 'NewConfirmed': 210, 'TotalConfirmed': 45490, 'NewDeaths': 13, 'TotalDeaths': 1725, 'NewRecovered': 23, 'TotalRecovered': 36145, 'Date': '2020-11-26T09:58:38Z', 'Premium': {}}
