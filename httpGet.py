import requests

headers = {'accept':'application/json', 'user-agent':'meuNavegador/0.1'}

client = requests.get('https://httpbin.org/html', headers=headers)

print("HTTP header:", client.headers)
print("Status code:", client.status_code)
print("Content:\n", client.text)
