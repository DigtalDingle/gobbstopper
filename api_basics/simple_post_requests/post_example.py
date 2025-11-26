import requests

# Simple POST request example
url = "https://httpbin.org/post"

payload = {
    "name": "Boss",
    "project": "Gobbstopper"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
