import argparse
import requests
from model import Folder
from pathlib import Path
import os

# Instruction How to run this file :  python uipath_upload_package_to_dest.py -u https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_ -t $token -f Process1 -fp /Users/chiragtagadiya/Downloads/RELearning2.1.0.3.nupkg 
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help=" orchestrator Base URL")
ap.add_argument("-t", "--token", required=True, help="Access Token to Authenticate for Source Environment orchestrator")
ap.add_argument("-f", "--fqp", required=True, help="Fully Qualified Path for Source Folder ")
ap.add_argument("-fp", "--file_path", required=True, help="Absolute path of File package which needs to be uploaded")


args = vars(ap.parse_args())
token = args.get('token')
fullyQualifiedFolderName = args.get('fqp')
url = args.get('url','https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_')
file_path = args.get('file_path')

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

    


def upload_package(feed_id:str, file_path:str):
    """
    Downloads the .nupkg file of a Package.

    Params:
        
        feed_id: str -> feedId for folder
        file_path:str -> Process Package Absolute path

    
    """

    try:

        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}',
            # requests won't add a boundary if this header is set when you pass files=
            # 'Content-Type': 'multipart/form-data',
        }

        params = {
            'feedId': feed_id
        }

        files = {
            'file': open(Path(file_path), 'rb')
        }

        response = requests.post(
            f'{url}/odata/Processes/UiPath.Server.Configuration.OData.UploadPackage',
            params=params,
            headers=headers,
            files=files
        )
        print(response.status_code)
        print(response.json())
    except Exception as exp:
        print("Error While Uploading Package")

folderId = get_folder_id(fullyQualifiedFolderName)
print(f"Folder ID : {folderId}")
feedId = get_feedId_for_folder(folderId)
print(f"For Folder {folderId} FeedId is {feedId}")


upload_res = upload_package(feedId, file_path)
print(upload_res)
# Download package from src ->
# 	authenticate using access_token
# 	get folderId based on fully_qualified_path
# 	Get Feed ID
# 		GET PROCESSED and fetch processID based on Version
# 	Download package based on process key and feed id


