import requests
from requests.auth import HTTPBasicAuth

client = requests.get('https://httpbin.org/basic-auth/gustavo/123456', auth=HTTPBasicAuth('gustavo', '123456'))

print("HTTP header:", client.headers)
print("Status code:", client.status_code)
print("Content:", client.text)
