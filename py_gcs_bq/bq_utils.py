from google.cloud import bigquery
from google.cloud.exceptions import NotFound, Conflict
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# PROJECT_ID = "my-first-project-123456-425801"
# DATASET_ID = 'etl_basics'
# TABLE_ID = 'fake_bank'

load_dotenv()

def create_dataset(client:bigquery.Client, dataset_id: str) -> None:
    try:
        dataset_ref = client.dataset(DATASET_ID)
        client.create_dataset(dataset_ref)
        logging.info(f"Dataset {DATASET_ID} created successfully!")
    except Conflict:
        logging.info("Dataset already exists, exitingnas successful")
    except Exception as e:
        logging.error(f"Encountered problem creating the Dataset {dataset_id}: {e}")
    