#### Assignment 02 ####

**Set up and Test Basic Postgres infrastructure with Docker**

#####In the assessment we are to create a postgres server leveraging docker and docker compose infrastructure, load data and be able to interact with Postgres from Python#####

**Step 1:**
#####Set up postgres infrastructure, create docker and docker compose file####

*A new local branch was created*
######cd into the root directory of your project
######git checkout -b feat/postgres_docker_init
######create a data folder and move your csv file into the data folder created
######create a folder for infra_scripts
######write your sql script for your table schema (HRANLY), write your table with the csv file structure
######write an sql script that will copy the csv file (HRANLY) into the DATA folder
######create docker compose file yaml - docker-compose.yaml that will configure your postgres server
######Run docker-compose up
######The above command will start the postgressql container, the docker compose will set up with the postgres service to initialize a database schema, creates a table, and load the data from a CSV file.

**Step 2:**
#####The postgres infrastructure set up should be able to interact with postgres server from Python

######Create a folder called 'src' that will hold your Python script
######import psycopg2
######pip install psycopg2 - Psycopg converts Python variables to SQL values
######pip freeze > requirements.txt
######import load_dotenv 
######Psycopg2: The function connect() creates a new database session and returns a new connection instance.
######The class connection encapsulates a database session which create a new cursor instances using the cursor() method to execute database commands and queries..
######Once the PostgreSQL service is running via Docker Compose, you can execute the Python script to fetch and print the data from the result





