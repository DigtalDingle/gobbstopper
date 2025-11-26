import requests

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if coin_id in data:
            return data[coin_id]["usd"]
        else:
            print("Coin not found in response.")
            return None

    except Exception as e:
        print("Error:", e)
        return None


# Example usage
coin = "bitcoin"
price = get_price(coin)

if price is not None:
    print(f"{coin.capitalize()} price: ${price}")
else:
    print("Could not fetch price.")
