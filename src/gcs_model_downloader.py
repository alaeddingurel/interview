from google.cloud import storage

class GCSModelDownloader:
    def __init__(self, bucket_name, model_blob_name, local_model_path):
        self.bucket_name = bucket_name
        self.model_blob_name = model_blob_name
        self.local_model_path = local_model_path

    def download_model(self):
        # Create a storage client
        storage_client = storage.Client()

        # Get the bucket
        bucket = storage_client.bucket(self.bucket_name)

        # Get blob
        blob = bucket.blob(self.model_blob_name)

        # Download blob to local file
        blob.download_to_filename(self.local_model_path)

        print(f"Model downloaded from {blob.name} in bucket {bucket.name}")
