import sys
import json
import requests

if len(sys.argv) == 1:
    sys.exit("command-line argument is not a number")

try:
    n = float(sys.argv[1])
except:
    print("command-line argument is not a number")
    exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    x = o["bpi"]
    y = x["USD"]
    z = y["rate_float"]
    amount = n * z
    print(f"${amount:,.4f}")
except requests.RequestException:
    exit()
