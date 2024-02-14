import yaml
import os
import random
import json

def get_random_file(directory):
    """
    Get a random file from the specified directory.
    """
    # List all files in the directory
    files = os.listdir(directory)
    print(files)

    #There could be folders and files here
    if files:
        return os.path.join(directory, random.choice(files))
    else:
        return None

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript_data = json.load(file)
    return transcript_data

def merge_transcript(transcript_data):
    merged_transcript = ""
    for step in transcript_data["conversation"]:
        speaker = step["speaker"]
        message = step["message"]
        merged_transcript += f"{speaker}: {message}\n"
    return merged_transcript

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data