from google.cloud import bigquery
from dotenv import load_dotenv
import os
import logging
import bq_utils
from bq_utils import create_dataset
import json


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

load_dotenv()

# PROJECT_ID = "my-first-project-123456-425801"
# DATASET_ID = 'etl_basics'
# TABLE_ID = ''

logging.info("Testing the logger!!")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"c:\Users\user\Downloads\alt-sch-gcs-key.json"
os.environ["GOOGLE_CLOUD_PROJECT"] = "my-first-project-123456-425801"


    



