import requests, json
token = 'test_IedZFNziR3ouohaV4nkDfPmMV39JSdg3KGMgisX_slV'

url = 'https://api.duffel.com/air/offer_requests'

headers = {"Accept-Encoding": "gzip", "Accept": "application/json", "Content-Type": "application/json", "Duffel-Version": "beta", "Authorization": "Bearer " + token}

data = {
  "data": {
    "passengers": [
      {
        "type": "adult"
      }
    ],
    "slices": [
      {
        "origin": "DFW",
        "destination": "AUS",
        "departure_date": "2020-12-03"
      }
    ],
    "cabin_class": "economy"
  }
}


req = requests.post(url, headers=headers, data=json.dumps(data))

for line in req.json()['data']['offers']:
    print(line['total_amount'], line['slices'][0]['segments'][0]['operating_carrier']['name'],
    line['slices'][0]['segments'][0]['departing_at'],
    line['slices'][0]['segments'][0]['arriving_at'])
