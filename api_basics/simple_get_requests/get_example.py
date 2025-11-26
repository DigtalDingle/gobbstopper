import requests

# Simple GET request example
url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
