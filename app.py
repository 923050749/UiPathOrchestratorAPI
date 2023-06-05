from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from auth import get_token
from db_utils import get_ticket_details_from_db, get_all_ticket_details_from_db
from exception import AuthenticationError, APIException
from auth import login_required_with_username_password, login_required_with_token
import requests
from config_entity import UseCase
from dataclasses import asdict
from uipath_folders_api import get_all_folders_from_orchestrator,\
             get_folders_by_id_from_orchestrator, create_new_folder
import json
load_dotenv()


host = os.environ.get('HOST')
port = os.environ.get('PORT')

app = Flask(__name__)

@app.route("/")
def home():
    return "UseCase Details : Automation of Code migration from Non-Production to Production"

@app.route('/api/Account/ays/Authenticate', methods=["POST"])
def get_token_ays_service_now():
    """
        Generate token for AYS Service now application

    """
    
    try:

        data = request.json
        username = data['username']
        password = data['password']
        request_acc = "ays"
        token = get_token(username, password, request_acc)
        if not token:
            raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)

        response_body ={
            "token":token[4],
            "status_code":200
        }
        return response_body
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error While processing request", status_code=500)


@app.route('/api/Account/aa/Authenticate', methods=["POST"])
def get_token_aa_control_room():
    """
        Acess to AA Control Room
        
    """
    
    try:
        data = request.json
        username = data['username']
        password = data['password']
        request_acc = "aa"

        # If VZ Team Provides proper credentials we will use below code 
        # url : http://<your_control_room_url>/v1/authentication
        # Automation Anywhere Authentication Method : STARTS
        # req_body = {
        #     "username": username,
        #     "password": password
        # }
        #aa_authentication_url='http://<your_control_room_url>/v1/authentication'
        # response = requests.post(aa_authentication_url, json=req_body)
        # response_body ={
        #     "token":response.json(),
        #     "status_code":response.status_code,
        #     "message":"Successfully Authenticated!!!"
        # }
        # Automation Anywhere Authentication Method : ENDS
        
        token = get_token(username, password, request_acc)
        if not token:
            raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)

        response_body ={
            "token":token[4],
            "status_code":200
        }
        return response_body
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error While processing request", status_code=500)

@app.route('/api/Account/aa1/Authenticate', methods=["POST"])
def get_token_aa1_control_room():
    """
        Acess to AA Control Room
        
    """
    
    try:
        data = request.json
        username = data['username']
        password = data['password']
        url = data['url']
        request_acc = "aa"

        # If VZ Team Provides proper credentials we will use below code 
        # url : http://<your_control_room_url>/v1/authentication
        # Automation Anywhere Authentication Method : STARTS
        req_body = {
            "username": username,
            "password": password
        }
        aa_authentication_url=f'http://{url}/v1/authentication'
        response = requests.post(aa_authentication_url, json=req_body)
        response_body ={
            "body":response.json(),
            "status_code":response.status_code
        }
        return response_body
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error While processing request", status_code=500)




    

# @app.route('/api/Account/uipath1/Authenticate', methods=["POST"])
# def get_token_uipath1_orchestrator():
#     """
#         Authenticate to UI Path Orchestrator
        
#     """
#     try:

#         data = request.json
#         url = data['url']
#         usernameOrEmailAddress = data['usernameOrEmailAddress']
#         password = data['password']
#         tenancyName=data['tenancyName']
#         request_acc = "UIPATH"

#         # UIPATH Orchestrator Authentication Method : STARTS

#         # If VZ Team Provides proper credentials we will use below code 
#         uipath_authentication_url = f'https://{url}/api/Account/Authenticate'
#         print(uipath_authentication_url)
#         req_body = {
#             "usernameOrEmailAddress": usernameOrEmailAddress,
#             "password": password,
#             "tenancyName":tenancyName
#         }
    
#         response = requests.post(uipath_authentication_url, json=req_body)
#         response_body ={
#             "response":response.json(),
#             "status_code":response.status_code
#         }

#         return response_body
        
#     except AuthenticationError as exp:
#         raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
#     except Exception as exp:
#         raise APIException("Internal Server Error While processing request", status_code=500)

@app.route('/api/Account/uipath/Authenticate', methods=["POST"])
def get_token_uipath_acc():
    """
        Authenticate to UI Path Orchestrator
        
    """
    try:
        print("processing")
        
        data = request.json
        print("data")
        print("+"*100)
        auth_url = data['url']
        tenancy_name = data['tenancy_name']

        
        # auth_url = f"https://account.uipath.com/oauth/token"
        
        auth_data = {
            "grant_type": data['grant_type'],
            "client_id": data['client_id'],
            "refresh_token": data['refresh_token']
        }
        auth_headers = {
            "Content-Type": "application/json",
            "X-UIPATH-TenantName": tenancy_name
        }
        
        try:
            auth_response = requests.post(auth_url, data=json.dumps(auth_data), headers=auth_headers)
            return auth_response.json()
        except Exception as exp:
            print(exp)
            raise Exception("Internal Server Processing Exception")

        
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        print(exp)
        raise APIException("Internal Server Error While processing request", status_code=500)





@app.route('/api/Account/digt/Authenticate', methods=["POST"])
def get_token_to_connect_digt():
    """
        Generate token for Accessing Digt Account

    """
    
    try:

        data = request.json
        username = data['username']
        password = data['password']
        request_acc = "digt"
        token = get_token(username, password, request_acc)
        if not token:
            raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)

        response_body ={
            "token":token[4],
            "status_code":200
            
        }
        return response_body

    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error While processing request", status_code=500)

@app.route('/api/Account/ays/ticket',methods=["GET"])
@login_required_with_username_password
def get_ays_usecase_details():
    """
        Get Usecase Details from AYS table 
        `uat_schema.atyourservice` table createdin DB with following columns based on RPA KT session videos and workflow
            task_Id : str
            task_name : str
            usecase_Id : str
            description : str
            comments : str
            LOB : str
            sub_LOB : str
            source_folder : str
            dest_folder : str
            task_status: str
    """
    try:
        ticket_number = request.args.get('ticket_number', type = str)
        print("ticket",ticket_number)

        ticket_details = get_ticket_details_from_db(ticket_number=ticket_number)
        if not ticket_details:
            status_code=404
            msg="UseCase Not found"
            raise APIException("UseCase Not found", status_code=404)
        ticket_body = {
            'task_Id':ticket_details[0],
            'task_name':ticket_details[1],
            'usecase_Id':ticket_details[2],
            'description':ticket_details[3],
            'comments':ticket_details[4],
            'LOB':ticket_details[5],
            'sub_LOB':ticket_details[6],
            'source_folder':ticket_details[7],
            'dest_folder':ticket_details[8],
            'task_status':ticket_details[9]
        }
        response_body = {
            'status_code':200,
            'body':ticket_body
        }
        return response_body
    

    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    

@app.route('/api/Account/ays1/ticket',methods=["GET"])
def get_ays1_usecase_details():
    """
        Use Service Now API for fetcing incident details
        
    """
    try:
        ticket_number = request.args.get('ticket_number', type = str)
        instance_name = request.args.get('instance_name', type = str)
        print("ticket_number", ticket_number)
        print("instance_name",instance_name)
        url = f'https://{instance_name}.service-now.com/api/now/table/incident'
        headers = {'Accept': 'application/json'}
        params = {'number': ticket_number}
        auth = request.authorization
        username=auth.username
        password=auth.password
        response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), params=params)
        ticket_body = response.json()['result'][0]
        response_body = {
            'status_code':200,
            'body':ticket_body
        }
        return response_body
    

    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error", 500)
    
@app.route('/api/Account/ays/tickets',methods=["GET"])
@login_required_with_username_password
def get_ays_all_usecase_details():
    """
        Get ALL Usecase Details from AYS table 
        `uat_schema.atyourservice` table createdin DB with following columns based on RPA KT session videos and workflow
            task_Id : str
            task_name : str
            usecase_Id : str
            description : str
            comments : str
            LOB : str
            sub_LOB : str
            source_folder : str
            dest_folder : str
            task_status: str
    """
    try:
        
        ticket_details = get_all_ticket_details_from_db()

        if not ticket_details:
            status_code=404
            msg="UseCase Not found"
            raise APIException("UseCase Not found", status_code=404)
        all_tickets=[]
        for ticket in ticket_details:
            ticket_body = UseCase(*ticket)
            all_tickets.append(asdict(ticket_body))

        response_body = {
            'status_code':200,
            'body':all_tickets
        }
        return response_body
    

    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    # except Exception as exp:
    #     if status_code is None:
    #         status_code = 500
    #     if msg is None:
    #         msg="Internal Server Error While processing request"

    #     raise APIException(msg, status_code=status_code)

@app.route('/api/Account/ays1/tickets',methods=["GET"])
def get_ays1_all_usecase_details():
    """
        Use Service Now API for fetcing incident details
        
    """
    try:
        
        

        instance_name = request.args.get('instance_name', type = str)
        
        print("instance_name",instance_name)
        url = f'https://{instance_name}.service-now.com/api/now/table/incident'
        headers = {'Accept': 'application/json'}
        
        auth = request.authorization
        username=auth.username
        password=auth.password
        response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password))
        ticket_body = response.json()['result']
        response_body = {
            'status_code':200,
            'body':ticket_body
        }
        return response_body
    

    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error", 500)


@app.route('/api/Account/uipath/folders',methods=["GET"])
def get_all_folders_uipath():
    try:
        #folder_id = request.args.get('folder_id', type = str)
        uipath_orchestrator_url = request.args.get('url', type = str)
        headers = request.headers
        bearer = headers.get('Authorization') 
        token = bearer.split()[1]
        all_folders = get_all_folders_from_orchestrator(token, uipath_orchestrator_url)
        response_body= {
            "folders":all_folders,
            "status_code":200
        }
        return response_body
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error", 500)


@app.route('/api/Account/uipath/folders',methods=["POST"])
def get_or_create_new_folder():
    try:
        
        # 'https://cloud.uipath.com/crkzqacgn/DefaultTenant/orchestrator_/odata/Folders'
        headers = request.headers
        bearer = headers.get('Authorization') 
        token = bearer.split()[1]

        new_folder_payload = request.json
        uipath_orchestrator_url = request.args.get('url', type = str)
        folder_create_response = create_new_folder(token, uipath_orchestrator_url, new_folder_payload)

        response_body ={
            "resource":folder_create_response.json(),
            "status_code":folder_create_response.status_code
        }
        return response_body
    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error", 500)


@app.route("/api/Account/uipath/move_src_to_dest", methods=["PUT"])
def move_code_from_src_to_dest():
    try:
        headers = request.headers
        bearer = headers.get('Authorization') 
        token = bearer.split()[1]
        base_orchestrator_url = request.args.get('url', type = str)
        src = request.args.get('src',type=int)
        tgt = request.args.get('tgt', type=int)



        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }

        params = {
            'targetParentId': f'{tgt}',
        }

        response = requests.put(
            f'{base_orchestrator_url}/odata/Folders({src})/UiPath.Server.Configuration.OData.MoveFolder',
            params=params,
            headers=headers,
        )
        
        return {"status_code":response.status_code}


    except AuthenticationError as exp:
        raise AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
    except Exception as exp:
        raise APIException("Internal Server Error", 500)
# Error Handling Route


@app.route("/redirect_url", methods=["POST","GET"])
def redirect_urls():
    header = request.headers
    print(request.args)
    print(header)
    return {"header":123}


@app.errorhandler(AuthenticationError)
def auth_error(err):
    return jsonify(err.to_dict()), err.status_code

@app.errorhandler(APIException)
def api_error(e):
    return e.to_dict(), e.status_code

if __name__=="__main__":
    app.run(debug=True, host=host, port=int(port))
