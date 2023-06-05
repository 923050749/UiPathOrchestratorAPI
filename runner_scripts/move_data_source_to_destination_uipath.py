
import requests
import argparse
from requests.auth import HTTPBasicAuth
import json



ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False, help="Get Orchestrator Base URL Detaisls")
ap.add_argument("-t", "--token", required=False, help="Get Orchestrator access token for authentication Detaisls")
ap.add_argument("-d", "--tgtfolder", required=False, help="Destination Folder ID ")
ap.add_argument("-s", "--srcfolder", required=False, help="Source Folder ID ")

args = vars(ap.parse_args())
url = args.get('url') or 'https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_'
token = args.get('token') or 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6Im1pdGhpLnRhZ2FkaXlhQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRmZmIwYzgxOTkyZTg5MTZmZjY2N2YiLCJhdWQiOlsiaHR0cHM6Ly9vcmNoZXN0cmF0b3IuY2xvdWQudWlwYXRoLmNvbSIsImh0dHBzOi8vdWlwYXRoLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODMxMjQyNjgsImV4cCI6MTY4MzIxMDY2OCwiYXpwIjoiOERFdjFBTU5YY3pXM3k0VTE1TEwzallmNjJqSzkzbjUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.AvzYfll_PkToYnt16WA70GV---vIh33fLqZcnwewghX337SUzTorY48moNfZToFnn0B-8kQeNKoMSB6dFvyoMcrXZMu5AG5jTIoGfBX162tw9YInTGJj2GgG_pwwmoyAF9zoAWi5N5SuWGmFQO0L9zF8xQNRep6sjE7kO3A5JmWCi-q7UaEaJW4bLWJMmGfKHYI7qr5T6ma3ZD-IkXp7Pdcaf8n49iuc9vUFhaFw2di0P4CPzlZfACqH1kJJ2qB3WCJ_m3xgJ5sKPUdymd7n_0z_i7CfV0dTvz1EaeF1Dvgk_OTCk1iVRWv9ZWeXjD_Kx1vVe31U7MuIcHJImrr-0Q'
srcfolder=args.get('srcfolder') or "4341482"
tgtfolder=args.get('tgtfolder') or "4341063"


headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}


# localhost:8999/api/Account/uipath/move_src_to_dest?url=https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_&src=4341500&tgt=4341325
response = requests.put(
    f'http://localhost:8999/api/Account/uipath/move_src_to_dest?url={url}&src={srcfolder}&tgt={tgtfolder}',
    headers=headers
)



print(response.json())
