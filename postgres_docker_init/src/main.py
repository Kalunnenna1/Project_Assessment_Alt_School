import psycopg2
import os
from dotenv import load_dotenv
import yaml
import json


load_dotenv()


# create a connection

def _get_pg_creds():
    return {
        'user': os.environ.get('POSTGRES_USER'),
        'password': os.environ.get('POSTGRES_PASSWORD'),
        'port': os.environ.get('POSTGRES_PORT, 5434'),
        'host': os.environ.get('POSTGRES_HOST', 'localhost'),
        'db_name': os.environ.get('POSTGRES_DB')
       
    }
    
def _start_postgres_connection():
    creds = _get_pg_creds()
    connection = psycopg2.connect(dbname=creds['db_name'],
                                         user=creds['user'],
                                         password=creds['password'],
                                         host=creds['host'],
                                         port=creds['port'])
    return connection

    print(result)
                    
def query_database(connection, query_str):
    conn = connection
    cursor = conn.cursor()
    cursor.execute (query_str)
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close
    
    return rows

if __name__ == "__main__":
    conn = _start_postgres_connection()
    query = """
        SELECT count(*) as total_reords
        FROM hranly
        """
        
    result = query_database(connection=conn, query_str=query)
    
    print(result)
                               

# create cursor
cursor = connection_object.cursor()

# use cursor to execute queries against postgres
cursor.execute("SELECT COUNT(*) FROM hranly;")

result = cursor.fetchall()

print(result)

# close the cursor & connection
cursor.close()
connection_object.close()
