# import requests
#
# api_username = "165e99c4bad271d20298f0661636fbcb"
# api_password = "1027db3a95605f877d17a2ae87807bbc"
# base_url = "https://api.intrinio.com"
#
# # Get the latest FY Income Statement for AAPL
# ticker = "AAPL"
# request_url = base_url + "/financials/standardized"
# query_params = {
#     'ticker': ticker,
#     'statement': 'income_statement',
#     'type': 'FY'
# }
#
# response = requests.get(request_url, params=query_params, auth=(api_username, api_password))
# if response.status_code == 401: print("Unauthorized! Check your username and password."); exit()
#
# data = response.json()['data']
#
# for row in data:
#     tag = row['tag']
#     value = row['value']
#     print(tag + ": " + str(value))

import intrinio
#
intrinio.client.username = ''
intrinio.client.password = ''

print(intrinio.prices('AAPL'))
#print(intrinio.companies('GOOG'))


#print(intrinio.companies(query='Popeyes'))




