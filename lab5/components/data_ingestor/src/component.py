import argparse
import logging
import sys
from pathlib import Path

from google.cloud import storage


def download_data(project_id, bucket, file_name, feature_path):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(file_name)
    # Creating the directory where the output file is created (the directory
    # may or may not exist).
    Path(feature_path).parent.mkdir(parents=True, exist_ok=True)
    blob.download_to_filename(feature_path)
    logging.info('Downloaded Data!')


# Defining and parsing the command-line arguments
def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id', type=str, help="GCP project id")
    parser.add_argument('--bucket', type=str, help="Name of the data bucket")
    parser.add_argument('--file_name', type=str, help="Name of the training data set file name")
    parser.add_argument('--feature_path', type=str, help="Name of the file to be used to store features")
    args = parser.parse_args()
    return vars(args)  # The vars() method returns the __dict__ (dictionary mapping) attribute of the given object.


if __name__ == '__main__':
    download_data(
        **parse_command_line_arguments())  # The *args and **kwargs is a common idiom to allow arbitrary number of
    # arguments to functions
