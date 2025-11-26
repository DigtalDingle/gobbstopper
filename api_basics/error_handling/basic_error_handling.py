import requests

# Basic error handling example
url = "https://api.github.com/nonexistent_endpoint"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx/5xx
    print(response.json())
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Request error:", e)
