import requests

url = "https://httpbin.org/status/400"  # This intentionally returns an error

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx or 5xx responses
    print("Success:", response.json())
except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)
except requests.exceptions.ConnectionError:
    print("Connection error — check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    print("An unexpected error occurred:", e)
