import psycopg2
import os


def connect(db_host, db_port, db_name, db_user, db_pwd):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
    
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pwd)
        
        print("Connection Established",conn)
        return conn
	
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
