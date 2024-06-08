import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Project Constants
PROJECT_ID = os.getenv("my-first-project-123456-425801")
BUCKET_NAME = os.getenv("alt_school_assessment_03")
PROJECT_ID = "my-first-project-123456-425801"
DATASET_ID = "etl_basics"
TABLE_ID = 'test'
FILE_PATH = "C:/Users/user/OneDrive/Desktop/F_semester/Project_Assessment_Alt_School/py_gcs_bq/data/test.csv"
SCHEMA_FILE_PATH = "C:/Users/user/OneDrive/Desktop/F_semester/Project_Assessment_Alt_School/py_gcs_bq/schemas/schema.json"
API_URL = "https://api.sampleapis.com/playstation/games"
LOCATION = "eu1"
# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)