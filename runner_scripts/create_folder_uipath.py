import requests
import argparse
from requests.auth import HTTPBasicAuth
import json



ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False, help="Get Orchestrator Base URL Detaisls")
ap.add_argument("-t", "--token", required=False, help="Get Orchestrator access token for authentication Detaisls")
ap.add_argument("-f", "--folder", required=False, help="Get Folder Name ")
ap.add_argument("-ft", "--feed_type", required=False, help="Get Folder Name ")

args = vars(ap.parse_args())
print(type(args))
print(args.keys())
url = args.get('url') or 'https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_'
token = args.get('token') or 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6Im1pdGhpLnRhZ2FkaXlhQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRmZmIwYzgxOTkyZTg5MTZmZjY2N2YiLCJhdWQiOlsiaHR0cHM6Ly9vcmNoZXN0cmF0b3IuY2xvdWQudWlwYXRoLmNvbSIsImh0dHBzOi8vdWlwYXRoLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODMxMjQyNjgsImV4cCI6MTY4MzIxMDY2OCwiYXpwIjoiOERFdjFBTU5YY3pXM3k0VTE1TEwzallmNjJqSzkzbjUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.AvzYfll_PkToYnt16WA70GV---vIh33fLqZcnwewghX337SUzTorY48moNfZToFnn0B-8kQeNKoMSB6dFvyoMcrXZMu5AG5jTIoGfBX162tw9YInTGJj2GgG_pwwmoyAF9zoAWi5N5SuWGmFQO0L9zF8xQNRep6sjE7kO3A5JmWCi-q7UaEaJW4bLWJMmGfKHYI7qr5T6ma3ZD-IkXp7Pdcaf8n49iuc9vUFhaFw2di0P4CPzlZfACqH1kJJ2qB3WCJ_m3xgJ5sKPUdymd7n_0z_i7CfV0dTvz1EaeF1Dvgk_OTCk1iVRWv9ZWeXjD_Kx1vVe31U7MuIcHJImrr-0Q'
folder_name=args.get('folder') or 'pqr667'
feed_type=args.get('feed_type') or "Processes"

print(feed_type)
print("+"*100)
import requests

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}

json_data = {
    'DisplayName': f'{folder_name}',
    "FolderType": "Standard",
    "ProvisionType": "Automatic",
    "PermissionModel": "FineGrained",
    # "ParentId": None,
    # "ParentKey": None,
    # "IsActive": True
    "FeedType": feed_type
}

response = requests.post(
    f'http://localhost:8999/api/Account/uipath/folders?url={url}/odata/Folders',
    headers=headers,
    json=json_data,
)

response_body= {
    "status_code":200,
    "body":response.json()
}

print(response_body)