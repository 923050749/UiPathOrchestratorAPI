
from psycopg2 import sql
from database import connect
from flask import jsonify, request
from exception import AuthenticationError
from functools import wraps

def check_auth_with_username_password(username, pwd, application='ays'):
    """
    Check if USername password are valid or not
    
    `users` Table columns
        username - string
        password - string
        request_account -string (UIPATH, AA)
        token - string
        tenancyName- string Default set to None
    


    Parameters
    ------------
        username: string
            User for AYS Service Now App
        pwd: string
            Password for USER
    Return
    -----------
        status : boolean
        True if Valid combination else False
    """
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        print("+++"*60)
        query = sql.SQL("SELECT * FROM uat_schema.users where username={username} and password={password} and application={application}").format(
                username=sql.Literal(username),
                password=sql.Literal(pwd),
                application = sql.Literal(application)
            )
        cur.execute(query=query)
        result = cur.fetchone()
        conn.close()
        if result is None:
            return False
        return True
    finally:
        if conn is not None:
            conn.close()
    
def check_auth_with_token(token):
    """
    Check if If Token is valid or not
    
    `users` Table columns
        token - string
        tenancyName- string Default set to None
    


    Parameters
    ------------
        token: string
            token for user for AYS Service Now App

    Return
    -----------
        status : boolean
        True if Valid combination else False
    """
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        
        
        query = sql.SQL("SELECT * FROM uat_schema.users where token={token}  ").format(
                    token=sql.Literal(token)
                )
        cur.execute(query=query)
        result = cur.fetchone()
        conn.close()
        if result is None:
            return False
        return True
    finally:
        if conn is not None:
            conn.close()
    



def get_token(username, pwd, request_account, tenancyName=None):
    """
    Generate token for AYS Service now application, , AA Control room, UIPATH orchestrator
    
    `users` Table columns
        username - string
        password - string
        request_account -string (UIPATH, AA)
        token - string
        tenancyName- string Default set to None
    


    Parameters
    ------------
        username: string
            User for AYS Service Now App
        pwd: string
            Password for USER
        request_account: string
            Request is for AA client or UIPath Orchestrator or AYS ?
        tenancyName - string 
            Default set to None, Present for UIPath
    Return
    -----------
        token : string
        Fetch token based on UserName, Password and request_account Param 
    """

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        if tenancyName:
            # This query is unique for UIPATH
            query = sql.SQL("SELECT * FROM uat_schama.users where username={username} and password={password} and request_account={request_account} and tenancy={tenancyName} ").format(
                    username=sql.Literal(username),
                    password=sql.Literal(pwd),
                    request_account=sql.Literal(request_account),
                    tenancyName=sql.Literal(tenancyName)
                )
        else:
            print(username, pwd, request_account)
            query = sql.SQL("SELECT * FROM uat_schema.users where username={username} and password={password} and application={request_account}").format(
                    username=sql.Literal(username),
                    password=sql.Literal(pwd),
                    request_account=sql.Literal(request_account)
                )
        print("Executing Query")
        cur.execute(query=query)
        result = cur.fetchone()
        conn.close()
        return result
    finally:
        if conn is not None:
            conn.close()
    




def login_required_with_username_password(fn):
    """
    Basic Authentication decorator for API for username password authentication
    
    """
    @wraps(fn)
    def required_auth_decorator(*args,**kwargs):
        auth = request.authorization
        
        if not auth or not check_auth_with_username_password(auth.username, auth.password, 'ays'):
            raise  AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
        return fn(*args, **kwargs)
    return required_auth_decorator

def login_required_with_token(fn):
    """
    Basic Authentication decorator for API for token authentication
    
    """
    @wraps(fn)
    def required_auth_decorator_fn(*args,**kwargs):
        auth = request.authorization
        if not auth or not check_auth_with_token(auth.token):
            raise  AuthenticationError("Password, UserName Account Combination MisMatched, You're not Authenticated!!", status_code=401)
        return fn(*args, **kwargs)
    return required_auth_decorator_fn