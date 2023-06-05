import requests
import argparse
from requests.auth import HTTPBasicAuth
import json


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--file_path", required=True, help="Get nupkg file path")
ap.add_argument("-t", "--token", required=True, help="Get Orchestrator access token for authentication Detaisls")
ap.add_argument("-f", "--folder", required=True, help="Get Folder Name to get Feed ID ")

args = vars(ap.parse_args())
print(type(args))
print(args.keys())
url = args.get('file_path') 
token = args.get('token') 
folder_name=args.get('folder')


headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {token}',
}

params = {
    'folderId': folder_name,
}

response = requests.get(
    'https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_/api/PackageFeeds/GetFolderFeed',
    params=params,
    headers=headers,
)
print(response.json())

headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {token}',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

params = {
    # 'feedId': 'ef21ff26-fa0a-448b-b8f7-f69d8557d43b',
    "feedId":response.json()
}

files = {
    'file': open(url, 'rb'),
}

response = requests.post(
    'https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_/odata/Processes/UiPath.Server.Configuration.OData.UploadPackage',
    params=params,
    headers=headers,
    files=files,
)
print(response.json())