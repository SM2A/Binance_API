import json
import requests

result = requests.get("https://api.binance.com/api/v3/exchangeInfo")

json_text = json.loads(result.text)

with open('exchangeInfo.json', 'w') as outfile:
    outfile.write(json.dumps(json_text, indent=4))
