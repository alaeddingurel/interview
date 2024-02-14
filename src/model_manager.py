from src.model_downloader import GCSModelDownloader, LocalModelChecker, HuggingFaceModelDownloader


class ModelManager:
    """
    This class is responsible for downloading and loading models from various sources
    Some of these sources are local, gcs bucket and huggingface hub
    """
    def __init__(self, bucket_name, model_name, local_model_path):
        self.bucket_name = bucket_name
        self.model_name = model_name
        self.local_model_path = local_model_path
        self.gcs_downloader = GCSModelDownloader(bucket_name, model_name, local_model_path)
        self.local_checker = LocalModelChecker(model_name, local_model_path)
        self.huggingface_downloader = HuggingFaceModelDownloader(model_name, local_model_path)

    def check_and_download_model(self):
        if self.local_checker.check_model_exists():
            print(f"Local model found for {self.model_name}.")
            model = self.local_checker.load_model()
            print(f"Model {self.model_name} has been loaded.")
            return model
        elif self.gcs_downloader.check_model_exists():
            print(f"Model {self.model_name} found in GCS bucket. Downloading...")
            self.gcs_downloader.download_model()
            model = self.gcs_downloader.load_model()
            print(f"Model {self.model_name} has been loaded.")
            return model
        elif self.huggingface_downloader.check_model_exists():
            model = self.huggingface_downloader.load_model()
            print(f"Model {self.model_name} found in HuggingFace Hub. Downloading...")
            print(f"Model {self.model_name} has been loaded.")
            return model
        else:
            print("Model not found.")
            return False