import argparse
import requests


def main():

    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'url': 'https://account.uipath.com/oauth/token',
        'grant_type': 'refresh_token',
        'client_id': '8DEv1AMNXczW3y4U15LL3jYf62jK93n5',
        'refresh_token': 'ATBwVe7MHXMWhcF7aZBfh5rVZiUwp8gcmv4YNu4fgi70t',
        'tenancy_name': 'DefaultTenant',
    }

    response = requests.post('http://localhost:8999/api/Account/uipath/Authenticate', headers=headers, json=json_data)

    response_body = {
        "status_code":response.status_code,
        "token_details":response.json()
    }
    print(response_body)
    return response_body

if __name__ == '__main__':
    response = main()