import requests
import json

def get_all_folders_from_orchestrator(token, uipath_orchestrator_url):
    """
    Fetch All Folders : Gets all folders or only the folders where user has SubFolders.View permission
    
    """
    
    folder_headers = {
        "Authorization": f"Bearer {token}",
        'Accept': 'application/json'
    }
    
    response = requests.get(uipath_orchestrator_url, headers=folder_headers)
    return response.json()
    
def get_folders_by_id_from_orchestrator(token, uipath_orchestrator_url, folder_id):
    """
    Fetch All Folders : Gets  folder or only the folder where user has SubFolders based on folder id
    
    """
    folder_url = f'{uipath_orchestrator_url}({folder_id})'
    
    folder_headers = {
        "Authorization": f"Bearer {token}",
        'Accept': 'application/json'
    }
    
    response = requests.get(folder_url, headers=folder_headers)
    return response

def create_new_folder(token, uipath_orchestrator_url, folder_req_body):
    """
    Create new folder on orchestrator
    """
    
    folder_headers = {
        "Authorization": f"Bearer {token}",
        'Accept': 'application/json'
    }
    response = requests.post(uipath_orchestrator_url, json=folder_req_body, headers=folder_headers)

    return response


