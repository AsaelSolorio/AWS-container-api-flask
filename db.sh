##DB.SH

#!/bin/bash

psql --host=aws-postgres-mydb.cvc8bgzmm0jz.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password=postgres -c "create database rest_api;" 

psql --host=aws-postgres-mydb.cvc8bgzmm0jz.us-east-1.rds.amazonaws.com --port=5432 --dbname=rest_api --username=postgres --password=postgres < db_movies.sql