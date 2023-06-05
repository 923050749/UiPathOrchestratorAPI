import psycopg2
import os
from dotenv import load_dotenv


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        load_dotenv()
        db_host=os.environ.get('DB_HOST')
        db_name = os.environ.get('DB_NAME')
        db_user = os.environ.get('DB_USER')
        db_pwd = os.environ.get('DB_PWD')
        db_port = os.environ.get('DB_PORT')
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


if __name__ == "__main__":
    connect()