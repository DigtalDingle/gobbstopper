import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Boss",
    "message": "Hello from Gobbstopper!"
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)

try:
    print("Response JSON:", response.json())
except ValueError:
    print("Response body was not valid JSON.")
