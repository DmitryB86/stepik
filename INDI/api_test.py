import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

params = {
  'access_key': 'b5525f496ac2231bb49155ada8237740'
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
print(api_response)
#
# for flight in api_response['results']:
#     if (flight['live']['is_ground'] is False):
#         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
#             flight['airline']['name'],
#             flight['flight']['iata'],
#             flight['departure']['airport'],
#             flight['departure']['iata'],
#             flight['arrival']['airport'],
#             flight['arrival']['iata']))
