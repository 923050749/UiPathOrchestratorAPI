import requests
import argparse

from requests.auth import HTTPBasicAuth


ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=False, help="Get username Detaisls")
ap.add_argument("-p", "--password", required=False, help="Get password Detaisls")


args = vars(ap.parse_args())

username = args.get('username') or "chirag"
password = args.get('password') or "password"

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'username': username,
    'password': password
    
}

response = requests.post('http://localhost:8999/api/Account/aa/Authenticate', headers=headers, json=json_data)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # If the response is OK, extract the token from the response body
    token = response.json().get('token')
    print('Token generated successfully: {}'.format(token))
else:
    # If the response is not OK, print an error message
    print('Error generating token: {}'.format(response.status_code))