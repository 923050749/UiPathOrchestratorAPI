import requests
import json

url = "https://account.uipath.com/oauth/token"

payload = json.dumps({
  "grant_type": "refresh_token",
  "client_id": "8DEv1AMNXczW3y4U15LL3jYf62jK93n5",
  "refresh_token": "ATBwVe7MHXMWhcF7aZBfh5rVZiUwp8gcmv4YNu4fgi70t",
  "tenancy_name": "DefaultTenant"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'UiPathSessionId=70906a8d-011b-4e51-9263-ded04fd76da7; __cf_bm=X0ymKD359sKq0dW1Lbcor7vQWVw0xzanL2rNRr0X_YA-1683675614-0-ASAUpbH5WXy0h2wV2Sh0BQoBhxDOu+fsAeCjeNJHwWn13egvHv+Dizd8EhBignLM9VWZD6/6jEqKWiKshW1PxL4=; __cf_bm=kEReF5zxbcNxkOGtwIxcN5nUrRfan32GldT3dlv5W_w-1683676021-0-AYDoGwj10nubNJm5y09SBPpI/PXHfPSpibZwdPnVpWBoCxTLRN1c68dT7XXD+LNvqkyM0V4ThEbU/1kcdb1NdSg=; did=s%3Av0%3A01081570-e853-11ed-af80-1f83909f7a09.6HOVdpx%2FIipdgwk5MIqhMPtzTYp5cTZWFP0e4a7XDb8; did_compat=s%3Av0%3A01081570-e853-11ed-af80-1f83909f7a09.6HOVdpx%2FIipdgwk5MIqhMPtzTYp5cTZWFP0e4a7XDb8'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
