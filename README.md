# TEB Case Project
This project is for the interview for TEB

TODO:

    - User will write a prompt in order to run the service.
    - command line command will take 
        - model name
        - model name
    - We'll check that whether this model exist or not. If not, then
        we need to download it from the Google Bucket.
        We don't use git-lfs etc because Git isn't good at managing the
        large files. For this reason, we don't add anything about the binary
        files into our commit history.
    - Service code will get the parameters from yaml file
        - Bucket Name etc.
    - We'll use FastAPI and We can also
        use Swagger as interface for our platform which is accessible via,
        https://localhost:port/docs
    
    - There is a need to write unit tests.


    - Code will check if model exists in the resources, there could be parameters which 
        checks user wants to use the resources only
        otherwise it will check the bucket,
        final option will be to check the Huggingface and download the model.


    - Candidate labels could be parametrized


Some Possible improvements:

    - OnnxRuntime Model
    - Bulk Inference



Available Models:
    
    - models--facebook--bart-base
    - facebook/bart-large-mnli 

    TODO:
        - we could add other models.


