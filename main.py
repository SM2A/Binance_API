import json
import requests

result = requests.get("https://api.binance.com/api/v1/exchangeInfo")

with open('exchangeInfo.json', 'w') as outfile:
    outfile.write(result.text)
