from google.cloud import storage
from google.api_core import page_iterator
from google.cloud import storage
import os


class GCSModelDownloader:
    def __init__(self, bucket_name, model_name, local_model_path):
        """
        Initializes a GCSModelDownloader instance.

        :param bucket_name: the name of the bucket to download the model
        :param model_name: the name of the model to download
        :param local_model_path: the name of the model to download

        """
        self.bucket_name = bucket_name
        self.model_name = model_name
        self.local_model_path = local_model_path
        # We're using anonymous client because our bucket is public
        self.storage_client = storage.Client.create_anonymous_client()

    def download_model(self):
        """
        Downloads a model from GCS bucket
        """

        # Get the bucket
        bucket = self.storage_client.bucket(self.bucket_name)

        # Get blob

        blobs = bucket.list_blobs(prefix=self.model_name)

        # Download blob to local file
        for blob in blobs:
            # Create the destination directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.join(self.local_model_path, blob.name)), exist_ok=True)

            # Download the blob to the local directory
            blob.download_to_filename(os.path.join(self.local_model_path, blob.name))

            print(f"Downloaded {blob.name} to {self.local_model_path}")


        print(f"Model downloaded from {blob.name} in bucket {bucket.name}")

    def check_model_exists(self):
        """
        Check if a model exists in the GCS bucket

        :param model_name: The name of the model
        :return: True if the model exists in the GCS bucket, False otherwise
        """

        # Get the bucket
        bucket = self.storage_client.bucket(self.bucket_name)

        # List objects in the bucket
        blobs = bucket.list_blobs()

        # We're getting the folder names
        # TODO: We don't need to check for each blob we could do the check for each iteration
        folders = set()
        for blob in blobs:
            # First folder is the name of the model
            folders.add(blob.name.split('/')[0])

        if self.model_name in folders:
            return True
        else:
            return False

    def check_model_download(self):
        if self.check_model_exists():
            self.download_model()
        else:
            print(f"Model {self.model_name} does not exist in bucket {self.bucket_name}")
class HuggingFaceModelDownloader:
    def __init__(self, model_name, local_model_path):
        self.model_name = model_name
        self.local_model_path = local_model_path

    def check_model_exists(self):
        pass

class LocalModelChecker:
    """
    Local model checker
    """
    def __init__(self, model_name, local_model_path):
        self.model_name = model_name
        self.local_model_path = local_model_path

    def check_model_exists(self):
        model_file_path = os.path.join(self.local_model_path, self.model_name)

        if os.path.exists(model_file_path):
            return True
        else:
            return False
