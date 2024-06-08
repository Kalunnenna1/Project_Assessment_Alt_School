from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
from google.cloud.exceptions import NotFound, Conflict
from dotenv import load_dotenv
import os
import logging
import json
from configuration import PROJECT_ID, DATASET_ID, TABLE_ID, FILE_PATH, SCHEMA_FILE_PATH

# Load environment variables
load_dotenv()

# Set project-specific constants
PROJECT_ID = "my-first-project-123456-425801"
DATASET_ID = "etl_basics"
TABLE_ID = 'test'
FILE_PATH = "C:/Users/user/OneDrive/Desktop/F_semester/Project_Assessment_Alt_School/py_gcs_bq/data/test.csv"
SCHEMA_FILE_PATH = "C:/Users/user/OneDrive/Desktop/F_semester/Project_Assessment_Alt_School/py_gcs_bq/schemas/schema.json"

client = bigquery.Client(project=PROJECT_ID)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Create dataset if it doesn't exist
try:
    dataset_ref = bigquery.Dataset(client.dataset(DATASET_ID))
    client.create_dataset(dataset_ref)
    logging.info(f"Dataset {DATASET_ID} created successfully!")
except Conflict:
    logging.info(f"Dataset {DATASET_ID} already exists.")
except GoogleAPIError as e:
    logging.error(f"Failed to create dataset {DATASET_ID}: {e}")

# Load schema from JSON file
try:
    with open(SCHEMA_FILE_PATH, 'r') as schema_file:
        schema = json.load(schema_file)
except FileNotFoundError as e:
    logging.error(f"Schema file not found: {e}")
except json.JSONDecodeError as e:
    logging.error(f"Error decoding JSON schema: {e}")

# Define the table reference
table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# Define the table using the schema
table = bigquery.Table(
    table_ref,
    schema=[bigquery.SchemaField.from_api_repr(field) for field in schema]
)

# Create table if it doesn't exist
try:
    client.create_table(table)
    logging.info(f"Table {TABLE_ID} created successfully in dataset {DATASET_ID}!")
except Conflict:
    logging.info(f"Table {TABLE_ID} already exists in dataset {DATASET_ID}.")
except GoogleAPIError as e:
    logging.error(f"Failed to create table {TABLE_ID}: {e}")

def insert_csv_file_into_table(
    client: bigquery.Client, table_ref: str, file_path: str, schema: list
) -> None:
    try:
        job_config = bigquery.LoadJobConfig(
            schema=[bigquery.SchemaField.from_api_repr(field) for field in schema],
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
        )

        logging.info("Starting to load CSV file into BigQuery table: %s", table_ref)
        with open(file_path, "rb") as source_file:
            load_job = client.load_table_from_file(
                source_file, table_ref, job_config=job_config
            )
        
        load_job.result()  # Wait for the job to complete
        logging.info("Loaded %d rows into %s", load_job.output_rows, table_ref)

    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON schema: %s", e)
    except GoogleAPIError as e:
        logging.error("BigQuery error: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

# Insert CSV file into the table
insert_csv_file_into_table(client, table_ref, FILE_PATH, schema)
