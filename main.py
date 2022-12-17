import json
import requests

result = requests.get("https://api.binance.com/api/v3/exchangeInfo")

json_text = json.loads(result.text)

if len(result.text) > 1000 :
    with open('exchangeInfoPretty.json', 'w') as outfile:
        outfile.write(json.dumps(json_text, indent=4))
    with open('exchangeInfoCompact.json', 'w') as outfile:
        outfile.write(result.text)
