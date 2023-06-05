from util.databasehelper import connect
import argparse
from getpass import getpass

# how to run script python .\connect_to_digit.py -i digtproduction.c5ogzsgipyri.us-east-1.rds.amazonaws.com -p 5432 -d digtprd -u automation -w


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--hostname", required=True, help="Get Hostname or IP where postgresql is running ")
ap.add_argument("-p", "--port", required=True, help="Get Port postgresql is running ")
ap.add_argument("-d", "--database", required=True, help="Get Postgresql database to connect with ")
ap.add_argument("-u", "--username", required=True, help="Username for database ")
ap.add_argument("-w", "--password", required=True, help="password for database ",  action='store_true', dest='password')


args = vars(ap.parse_args())
password = getpass()
username = args.get('username')
port = args.get('port')
database = args.get('database')
host = args.get('hostname')
try:
    conn = connect(host, port, database, username, password)
    print("connection Established")
    print("+"*80)
    cur = conn.cursor()
    cur.execute("select count(*) from digt.coe_usecase_automation")
    

    print("Total Number of UseCase in Digt ",cur.fetchone())
    cur.close()
    conn.close()
except Exception as exp:
    print("Error in connecting with Database", exp)
finally:
    if conn:
        conn.close()

