import argparse
import requests
from model import Folder
from pathlib import Path
import os

# Instruction How to run this file :  python uipath_download_package_from_src.py -t eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6Im1pdGhpLnRhZ2FkaXlhQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRmZmIwYzgxOTkyZTg5MTZmZjY2N2YiLCJhdWQiOlsiaHR0cHM6Ly9vcmNoZXN0cmF0b3IuY2xvdWQudWlwYXRoLmNvbSIsImh0dHBzOi8vdWlwYXRoLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODM4NjM5NjQsImV4cCI6MTY4Mzk1MDM2NCwiYXpwIjoiOERFdjFBTU5YY3pXM3k0VTE1TEwzallmNjJqSzkzbjUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.Wz-TlDYc_k2Agjs5OvGz8JYx_zhfP7ZDIjcn3UCfFwi-2iD3rB4Ul-9_kTOJCdXoV7p0KLstGHQIzQr-AC0dyxXj_QD6BGDbx78wZQZnyY0npzSymOORoeAbUOONjOQNn6zgCytr9YQWpMoA0AXaOVNFDNNgeOZ2wu8a3fb1sg69aSDh8JwJ8iFFV79gYsFzEcnjkIr1BUPde7yd9KjhErqMNu5FYw8kUl_ltanodJalagn3anUvchzg6Z41RQyzLqq6uhxpiLm6fVK3vnQKGVhEZjRDjY8nNcoG-nXnuU_gcaEIigXZVct3INpC6eh8QIBn7adPePf5nPGZd4m_6g -f VBG_DEV/VBG1_DEV/UC1/Performer_dev -u https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_ -p RELearning2:1.0.2
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help=" orchestrator Base URL")
ap.add_argument("-t", "--token", required=True, help="Access Token to Authenticate for Source Environment orchestrator")
ap.add_argument("-f", "--fqp", required=True, help="Fully Qualified Path for Source Folder ")
ap.add_argument("-p", "--process_key", required=True, help="ProcessId for FolderPackage e.g PackgeName:PackageVersion")


args = vars(ap.parse_args())
token = args.get('token')
fullyQualifiedFolderName = args.get('fqp')
url = args.get('url','https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_')
process_key = args.get('process_key')

def get_folder_id(fqn:str):
    """
    Get Folder Id from Folder's fully qualified  Path
    
    """
    try:


        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}',
        }

        response = requests.get(f'{url}/odata/Folders', headers=headers)

        folders_data = response.json()['value']
        
        for folder_detail in folders_data:

            if folder_detail['FullyQualifiedName'] ==fqn:
                return folder_detail['Id']
        return f"There is No Folder with FullyQualifiedFolder Path {fqn}"

    except Exception as exp:
        print("Exception getting FolderID")



def get_feedId_for_folder(folder_id:int):
    """
    Get Feed Id for Folder
    """
    try:
        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}',
        }

        params = {
            'folderId': folder_id
        }

        response = requests.get(
            f'{url}/api/PackageFeeds/GetFolderFeed',
            params=params,
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        return None
        

    except Exception as exp:
        print(exp)
        print(f"Exception getting FeedId for Folder Id {folder_id}")

    


def download_package(process_key:str, feed_id:str):
    """
    Downloads the .nupkg file of a Package.

    Params:
        process_key:str -> ProcessID:Process_version
        feed_id: str -> feedId for folder

    
    """

    try:
        

        headers = {
            'accept': 'application/octet-stream',
            'authorization': f'Bearer {token}',
        }

        params = {
            'feedId': feed_id
        }
        print(process_key)
        response = requests.get(
            f"{url}/odata/Processes/UiPath.Server.Configuration.OData.DownloadPackage(key='{process_key}')",
            params=params,
            headers=headers,
        )

        if response.status_code == 200:

            file_path = Path(os.getcwd(),f'{process_key}.nupkg' )
            with open(file_path,'wb') as out_file:
                out_file.write(response.content)
            print(response.status_code)
            print(f"File downloaded at {file_path}")
            return file_path
        else:
            print(f"response status code {response.status_code}")
            print("Error while Downloading Packge")
            return None
    except Exception as exp:
        print("Error While Downloading Package")

folderId = get_folder_id(fullyQualifiedFolderName)
print(f"Folder ID : {folderId}")
feedId = get_feedId_for_folder(folderId)
print(f"For Folder {folderId} FeedId is {feedId}")

file_path = download_package(process_key, feedId)
print("Downloaded File Path :",file_path)



