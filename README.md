         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


# AWS-container-api-Flask
We are going to Create an API-REST Container in AWS Cloud9 and Publish to Docker Hub and Push to ECR-AWS

## This API-REST is developed for Linux-alpine Architecture
if you want to use it for Ubuntu distribution replace the next commands
``` batch
sudo apk add == sudo apt install 
```

next, run the next command first
``` batch
docker compose up airflow-init
```
next, you run the next command for the rest of the airflow-services
``` batch
docker compose up 
```
if everything is ok. you will have the next folders created. inside the ./dags folder you create your dags using python 

``` batch
./dags
./logs
./plugins 
```

## Build Docker ETL Pipeline using Airflow

### Scenario

We will build a Restful Flask CRUD API about Movies.

We will create a database using POSTGRES hosted in AWS-RDS instance to store information about movies. we will import the psycopg2-binary library and configure it. The name of our database file will be database/db.py , if you want to use another RDS, do the setup. 

- Extract data from a csv file
- Extract data from a tsv file
- Extract data from a fixed width file
- Transform the data
- Load the transformed data into the staging area

you can download the raw data using the next command


``` batch
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz
```
The final csv file should use the fields in the order given below:

``` batch
Rowid, Timestamp, Anonymized Vehicle number, Vehicle type, Number of axles, Tollplaza id, Tollplaza code, Type of Payment code, and Vehicle Code
```

- install the "requirements.txt" file
``` batch
pip install -r requirements.txt
```

Check data and info inside Airflow container bash 
``` batch
docker exec -it [container_name] bash
```
