## 1. Connect to DIGT DATABASE

    

    -i HOSTNAME, --hostname HOSTNAME
                            Get Hostname or IP where postgresql is running

    -p PORT, --port PORT  Get Port postgresql is running

    -d DATABASE, --database DATABASE
                             Get Postgresql database to connect with

    -u USERNAME, --username USERNAME
                             Username for database

    -w, --password        password for database

    * below command will connect to database, if successfuly connected then return count of total number of digt usecases

```
python .\connect_to_digit.py -i digtproduction.c5ogzsgipyri.us-east-1.rds.amazonaws.com -p 5432 -d digtprd -u automation -w
```


## 2. Check AYS Usecase status in DIGT

    -t USECASE_ID, --usecase_id USECASE_ID
                    usecase id

    -i HOSTNAME, --hostname HOSTNAME
                    Get Hostname or IP where postgresql is running

    -p PORT, --port PORT  Get Port postgresql is running

    -d DATABASE, --database DATABASE
                    Get Postgresql database to connect with

    -u USERNAME, --username USERNAME
                    Username for database

    -w, --password        password for database

    -s STATUS_CD, --status_cd STATUS_CD
                    Which Status we are checking : DEVREADY, HOLD, UCAPPROVAL , UAT, DEVAPPROVAL,    
                    PRODDEPLOY, PRODREADY, DRAFT, FINALSECLGL, CANCELLED, PRODUCTION, DEVELOP,       
                    RETIRED, PRODDRYRUN, ANALYSIS

    * -s (--status_cd) is optional by default we will check for 'PRODREADY' status_cd

    * this method check if usecase_id has valid status or not 
    * below command will check if usecase_id UC4389 has status_code PRODREADY or not
```    
python .\ays_check_status_for_approval.py -i digtproduction.c5ogzsgipyri.us-east-1.rds.amazonaws.com -p 5432 -d digtprd -u automation -t UC4389 -s PRODREADY -w
```