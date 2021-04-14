import requests

headers = {'accept':'image/png'}

client = requests.get('https://httpbin.org/image', headers=headers)

print("HTTP header:", client.headers)
print("Status code:", client.status_code)
print("Image size:", len(client.content), "bytes")

f = open("image.png", "wb")
f.write(client.content)
f.close()
