from src.model_downloader import GCSModelDownloader, LocalModelChecker, HuggingFaceModelDownloader


class ModelManager:
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
        else:
            print("Model not found.")
            return False


#if __name__ == '__main__':
#    model = ModelManager("bart-model", "models--facebook--bart-basec", local_model_path="../resources/").check_and_download_model()
#    print(model)