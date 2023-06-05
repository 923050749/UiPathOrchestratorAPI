import argparse
import requests
from model import Folder

import json
        
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help=" orchestrator Base URL")
ap.add_argument("-t", "--token", required=True, help="Access Token to Authenticate for Source Environment orchestrator")
ap.add_argument("-f", "--fqp", required=True, help="Fully Qualified Path for Source Folder ")
ap.add_argument("-p", "--process_Id", required=True, help="ProcessId for FolderPackage")


args = vars(ap.parse_args())
token = args.get('token')
fullyQualifiedFolderName = args.get('fqp')
version = args.get('version')
url = args.get('url','https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_')
process_Id = args.get('process_Id')

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

    


def get_all_process_versions(processId: str, feed_id:str):
    """
    Returns a collection of all available versions of a given process. 

    Params:
        processId:str -> process ID [Title]
        feed_id: str -> feedId

    """
    try:
        

        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}',
        }

        params = {
            'feedId': {feed_id},
            '$orderby':'Published'
        }
        print(processId)
        response = requests.get(
            f"{url}/odata/Processes/UiPath.Server.Configuration.OData.GetProcessVersions(processId='{processId}')",
            params=params,
            headers=headers
        )
        
        all_versions = response.json()
        ret_res = {}
        ret_res['total_versions'] = all_versions['@odata.count']
        ret_res['versions'] =[]
        for ver_det in all_versions['value']:
            ver_out = {}
          
            ver_out['Id']=ver_det['Id']
            ver_out['Key'] = ver_det['Key']
            ver_out['Title']=ver_det['Title']
            ver_out['Version']=ver_det['Version']
            ver_out['Description']=ver_det['Description']
            ver_out['Published']=ver_det['Published']
            ret_res['versions'].append(ver_out)
 
        return ret_res
    except Exception as exp:
        print("Error fetching All the processes for Given ProcessID and Given FeedID")

def download_package(process_key:str, feed_id:str):
    """
    Downloads the .nupkg file of a Package.

    Params:
        process_key:str -> ProcessID:Process_version
        feed_id: str -> feedId for folder

    
    """

folderId = get_folder_id(fullyQualifiedFolderName)
print(f"Folder ID : {folderId}")
feedId = get_feedId_for_folder(folderId)
print(f"For Folder {folderId} FeedId is {feedId}")
all_versions = get_all_process_versions(process_Id, feedId)

print(json.dumps(all_versions, indent=4))
# Download package from src ->
# 	authenticate using access_token
# 	get folderId based on fully_qualified_path
# 	Get Feed ID
# 		GET PROCESSED and fetch processID based on Version
# 	Download package based on process key and feed id