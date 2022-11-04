import json
import requests

result = requests.get("https://api.binance.com/api/v3/exchangeInfo")

with open('exchangeInfo.json', 'w') as outfile:
    outfile.write(result.text)
