from util.databasehelper import connect
import argparse
from getpass import getpass
from psycopg2 import sql

# how to run script => python .\ays_check_status_for_approval.py -i digtproduction.c5ogzsgipyri.us-east-1.rds.amazonaws.com -p 5432 -d digtprd -u automation -t UC4389 -s PRODREADY -w


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--usecase_id", required=True, help="usecase id")
ap.add_argument("-i", "--hostname", required=True, help="Get Hostname or IP where postgresql is running ")
ap.add_argument("-p", "--port", required=True, help="Get Port postgresql is running ")
ap.add_argument("-d", "--database", required=True, help="Get Postgresql database to connect with ")
ap.add_argument("-u", "--username", required=True, help="Username for database ")
ap.add_argument("-w", "--password", required=True, help="password for database ",  action='store_true', dest='password')
ap.add_argument("-s", "--status_cd", required=False, help='Which Status we are checking : \
                 DEVREADY, HOLD, UCAPPROVAL , UAT, DEVAPPROVAL, PRODDEPLOY, PRODREADY, DRAFT, FINALSECLGL, CANCELLED, PRODUCTION, DEVELOP, RETIRED, PRODDRYRUN, ANALYSIS',\
                    default='PRODREADY')




try:
    args = vars(ap.parse_args())

    usecase_id = args.get('usecase_id')
    status_cd = args.get('status_cd','PRODREADY')
    password = getpass()
    username = args.get('username')
    port = args.get('port')
    database = args.get('database')
    host = args.get('hostname')
    print("Trying to Connect to DIGT database")
    conn = connect(host, port, database, username, password)
    #print("connection Object",conn)

    
    cur = conn.cursor()

    query = sql.SQL("SELECT * from digt.coe_usecase_automation where ucase_id ={usecase_id} and status_cd={status_cd};").format(
                usecase_id=sql.Literal(usecase_id),
                status_cd=sql.Literal(status_cd)
            )
    cur.execute(query=query)
    result = cur.fetchone()
    conn.close()
    # result format => (ucase_id, pillar_id, status_cd, description, comment)
    print("+"*80)
    print("fetching usecase status from digt")
    print("+"*80)
    if result:
        print(f"Usecase Id {result[0]} status in DIGT => {result[2]}", )
    else:
        print(f"No Record Found with UsecaseId  {usecase_id} and status_code {status_cd} in digt  ")
except Exception as exp:
    print("Error in connecting with Database", exp)
finally:
    if conn:
        conn.close()
