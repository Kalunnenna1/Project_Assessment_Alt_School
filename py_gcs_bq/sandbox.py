from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"c:\Users\user\Downloads\alt-sch-gcs-key.json"
os.environ["GOOGLE_CLOUD_PROJECT"] = "my-first-project-123456-425801"

# Initialize the Google Cloud Storage client
gcs_client = storage.Client()

# create a client
gcs_client = storage.Client()

# use the client to interact with gcs


# list buckets

#for bucket in gcs_client.list_buckets():
 #   print(bucket.name)
    
for bucket in gcs_client.list_buckets():
    if bucket.name == 'alt_school_assessment_03':
        print(f"found the bucket!!: {bucket.name}")

# # create a bucket
# # BUCKET_NAME='alt_school_assessment_03'
# # location = 'eu'
# storage_class = 'STANDARD'

# gcs_client = storage.Client()
# bucket = gcs_client.bucket(BUCKET_NAME)
# bucket.storage_class = storage_class
# bucket.location = location
# bucket.create()

# upload file to the bucket
#file_path ='..\..\data\test.csv'
#bucket = gcs_client.bucket(BUCKET_NAME)
#blob = bucket.blob(blob_name)
#blob_upload_from_file(file_path)


# Define the bucket name and the blob name
BUCKET_NAME = 'alt_school_assessment_03'
blob_name = 'test.csv'
FILE_PATH = "C:/Users/user/OneDrive/Desktop/F_semester/Project_Assessment_Alt_School/py_gcs_bq/data/test.csv"
bucket = gcs_client.bucket(BUCKET_NAME)
blob = bucket.blob(blob_name)

# Upload the file to GCS
blob.upload_from_filename(FILE_PATH)

print(f'File {FILE_PATH} uploaded to {blob_name} in bucket {BUCKET_NAME}.')    
  

 
    
# Create bucket




#download a file to the bucket
# file_path = 'C:\Users\user\OneDrive\Desktop\F_semester\Project_Assessment_Alt_School\py_gcs_bq\data\test.csv'
