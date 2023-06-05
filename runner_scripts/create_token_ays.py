import requests
import argparse
import requests
from requests.auth import HTTPBasicAuth


ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=False, help="Get Username Detaisls")
ap.add_argument("-p", "--password", required=False, help="Get password Detaisls")



args = vars(ap.parse_args())
username = args.get('username') or "chirag"
password=args.get('password') or "password"

data = {
    'username': username,
    'password': password
}


# Define the API endpoint URL for token generation
token_url = 'http://localhost:8999/api/Account/ays/Authenticate'

# Set the request headers and body with your credentials
headers = {
    'Content-Type': 'application/json'
}



# Send an HTTP POST request to the API endpoint
response = requests.post(token_url, headers=headers, json=data)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # If the response is OK, extract the token from the response body
    token = response.json().get('token')
    print('Token generated successfully: {}'.format(token))
else:
    # If the response is not OK, print an error message
    print('Error generating token: {}'.format(response.status_code))