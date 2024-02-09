from google.cloud import storage
from google.api_core import page_iterator
from google.cloud import storage


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
        blob = bucket.blob(self.model_name)

        # Download blob to local file
        blob.download_to_filename(self.local_model_path)

        print(f"Model downloaded from {blob.name} in bucket {bucket.name}")

    def check_model_exists(self, model_name):
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

        if model_name in folders:
            return True
        else:
            return False

    def check_model_download(self):
        if self.check_model_exists(self.model_name):
            self.download_model()
        else:
            print(f"Model {self.model_name} does not exist in bucket {self.bucket_name}")




if __name__ == '__main__':
    gcs_downloader = GCSModelDownloader("bart-model", "models--facebook--bart-base", local_model_path="../resources")
    is_in_bucket = gcs_downloader.check_model_exists("models--facebook--bart-base")
    print(is_in_bucket)