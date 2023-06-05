import argparse
import requests
from requests.auth import HTTPBasicAuth
import json


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--ticket_number", required=False, help="Get Ticket Detaisls")
ap.add_argument("-u", "--username", required=False, help="Get Ticket Detaisls")
ap.add_argument("-p", "--password", required=False, help="Get Ticket Detaisls")



args = vars(ap.parse_args())
ticket_number = args.get('ticket_number') or 'uc0001'
username = args.get('username') or 'chirag'
password=args.get('password') or "password"

params = {
    'ticket_number': ticket_number
}

response = requests.get('http://localhost:8999/api/Account/ays/ticket', auth=HTTPBasicAuth(username, password), params=params)

response_body = {
    "output" : response.json()
}


print(response_body)
