import requests
import json

url = "https://www.sec.gov/files/company_tickers.json"

# SEC requires a User-Agent header
headers = {
    "User-Agent": "Yinuo yinuo_l@foxmail.com"
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # error if request failed

data = response.json()

# Extract ticker
list_ticker = []

for entry in data.values():
    list_ticker.append(entry["ticker"])

# save to a file:
with open("list_ticker.json", "w") as f:
    json.dump(list_ticker, f, indent=2)
