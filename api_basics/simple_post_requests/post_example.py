import requests

url = "https://api.github.com"

response = requests.get(url, headers={"User-Agent": "gobbstopper-demo"})

print("Status:", response.status_code)

try:
    print("Body:", response.json())
except ValueError:
    print("Body is not valid JSON.")
