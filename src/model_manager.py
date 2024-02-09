from src.gcs_model_downloader import GCSModelDownloader, LocalModelChecker, HuggingFaceModelDownloader

class ModelManager:
    def __init__(self, bucket_name, model_name, local_model_path):
        self.gcs_downloader = GCSModelDownloader(bucket_name, model_name, local_model_path)
        self.local_checker = LocalModelChecker(model_name, local_model_path)
        self.huggingface_downloader = HuggingFaceModelDownloader(model_name, local_model_path)

    def check_and_download_model(self):
        if self.local_checker.check_model_exists():
            print("Local model found.")
            return True
        elif self.gcs_downloader.check_model_exists():
            print("Model found in GCS bucket. Downloading...")
            self.gcs_downloader.download_model()
            return True
        else:
            print("Model not found.")
            return False


if __name__ == '__main__':
    manager = ModelManager("bart-model", "models--facebook--bart-base", local_model_path="../resources/")
    manager.check_and_download_model()

