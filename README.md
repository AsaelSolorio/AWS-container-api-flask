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

next, create a virtual venv
``` batch
python -m venv venv
source venv/bin/activate
```
next, you go to Flask_CRUD folder where you can scaffold the Makefile to install all the libraries
``` batch
cd Flask_CRUD
make install
```
## Scenario

We will build a Restful Flask CRUD API about Movies.

We will create a database using POSTGRES hosted in AWS-RDS instance to store information about movies. we will import the psycopg2-binary library and configure it. The name of our database file will be database/db.py , if you want to use another RDS, do the setup. 

We will be using the HTTP methods through Insomnia requests

- GET
- POST
- PUT
- DELETE

Check data and info inside Docker Hub and ECR-AWS

### images

https://github.com/AsaelSolorio/AWS-container-api-flask/issues/1#issuecomment-1688341803

https://github.com/AsaelSolorio/AWS-container-api-flask/issues/1#issuecomment-1688342767


