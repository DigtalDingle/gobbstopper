import requests

# Simple crypto price fetcher
url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    btc_price = data.get("bitcoin", {}).get("usd")
    print("Bitcoin Price (USD):", btc_price)
else:
    print("Error fetching price:", response.status_code)
