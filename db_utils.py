
from psycopg2 import sql
from database import connect
from flask import jsonify
from exception import AuthenticationError, APIException


def get_ticket_details_from_db(ticket_number):

    """
    Fetch Ticket details from database
    `usecase` Table columns
        ticket_number - string
        short_desc - string
        long_desc - string
        short_desc - string
        digital_lead - string
        sec_leg_approval - boolean
        dev_approval - boolean
        uat_approval - boolean
        prod_approval - boolean
        attachment_id - string
    


    Parameters
    ------------
        ticket_number: string
            ticket_number is identifier in usecase table
        
    Return
    -----------
        ticket_details : object 
    """
    
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        print("ticket_number",ticket_number)
        query = sql.SQL("SELECT * FROM uat_schema.atyourservice where \"usecase_id\"={ticket_number} ").format(
                    ticket_number=sql.Literal(ticket_number)
                )
        cur.execute(query=query)
        # cur.execute(f"select * from uat_schema.atyourservice where \"usecase_Id\" = '{ticket_number}'")
        result = cur.fetchone()
        conn.close()
        return result
    except Exception as exp:
        print(exp)
        raise APIException("Error while fetching ticker details", status_code=500)
    finally:
        if conn is not None:
            conn.close()
    


def get_all_ticket_details_from_db():
    """
    Fetch ALL Ticket details from database
    `usecase` Table columns
        ticket_number - string
        short_desc - string
        long_desc - string
        short_desc - string
        digital_lead - string
        sec_leg_approval - boolean
        dev_approval - boolean
        uat_approval - boolean
        prod_approval - boolean
        attachment_id - string
    


    Parameters
    ------------
        ticket_number: string
            ticket_number is identifier in usecase table
        
    Return
    -----------
        List[ticket] : list of tickets 
    """
    
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        query = sql.SQL("SELECT * FROM uat_schema.atyourservice ")
        cur.execute(query=query)
        result = cur.fetchall()
        conn.close()
        return result
    except Exception as exp:
        raise APIException("Error while fetching ticker details", status_code=500)
    finally:
        if conn is not None:
            conn.close()