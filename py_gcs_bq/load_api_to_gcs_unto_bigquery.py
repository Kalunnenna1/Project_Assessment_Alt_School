import requests
import json
from google.cloud import storage
from google.cloud import bigquery

# Define the API URL
API_URL = "https://sampleapis.com/api-list/playstation"

# Fetch data from the API
response = requests.get(API_URL)

# Check if response is successful
if response.status_code == 200:
    try:
        data = response.json()
        if data:
            # Convert data to JSON Lines format
            json_lines_data = '\n'.join([json.dumps(record) for record in data])

            # Upload data to GCS
            def upload_to_gcs(bucket_name, destination_blob_name, data):
                client = storage.Client()
                bucket = client.bucket(bucket_name)
                blob = bucket.blob(destination_blob_name)

                blob.upload_from_string(data, content_type='application/json')
                print(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}.")

            BUCKET_NAME = "gcs_to_bigquery"
            DESTINATION_BLOB_NAME = "play_station.jsonl"

            upload_to_gcs(BUCKET_NAME, DESTINATION_BLOB_NAME, json_lines_data)

            # Load data from GCS to BigQuery
            def load_data_from_gcs_to_bq(project_id, dataset_id, table_id, gcs_uri, schema_file_path):
                client = bigquery.Client(project=project_id)
                dataset_ref = client.dataset(dataset_id)
                table_ref = dataset_ref.table(table_id)

                # Load schema from JSON file
                with open(schema_file_path, 'r') as schema_file:
                    schema = json.load(schema_file)
                
                table_schema = [bigquery.SchemaField.from_api_repr(field) for field in schema]

                job_config = bigquery.LoadJobConfig(
                    schema=table_schema,
                    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
                )

                load_job = client.load_table_from_uri(
                    gcs_uri,
                    table_ref,
                    job_config=job_config
                )

                load_job.result()  # Waits for the job to complete
                print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")

            PROJECT_ID = "my-first-project-123456-425801"
            DATASET_ID = "gcs_bq"
            TABLE_ID = "playstation_games"
            GCS_URI = f"gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}"
            SCHEMA_FILE_PATH = "py_gcs_bq/schemas/playstation_games_schema.json"

            load_data_from_gcs_to_bq(PROJECT_ID, DATASET_ID, TABLE_ID, GCS_URI, SCHEMA_FILE_PATH)
        else:
            print("Error: API response is empty.")
    except json.JSONDecodeError:
        print("Error: The API response is not in valid JSON format.")
else:
    print(f"Error: Failed to fetch data from the API. Status code: {response.status_code}")
