import argparse
import json
import logging
import os
import sys
from pathlib import Path

import pandas as pd
from google.cloud import storage
from keras.layers import Dense
from keras.models import Sequential


def train_mlp(project_id, feature_path, model_repo, metrics_path):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    df = pd.read_csv(feature_path, index_col=None)

    logging.info(df.columns)

    # split into input (X) and output (Y) variables
    X = df.loc[:, ['ntp', 'age', 'bmi', 'dbp', 'dpf', 'pgc', 'si', 'tsft']].values
    Y = df.loc[:, ['class']].values
    # define model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
    # evaluate the model
    scores = model.evaluate(X, Y, verbose=0)
    logging.info(model.metrics_names)
    metrics = {
        "accuracy:": scores[1],
        "loss": scores[0],
    }

    # Save the model locally
    local_file = '/tmp/local_model.h5'
    model.save(local_file)
    # Save to GCS as model.h5
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(model_repo)
    blob = bucket.blob('model.h5')
    # Upload the locally saved model
    blob.upload_from_filename(local_file)
    # Clean up
    os.remove(local_file)
    print("Saved the model to GCP bucket : " + model_repo)
    # Creating the directory where the output file is created (the directory
    # may or may not exist).
    Path(metrics_path).parent.mkdir(parents=True, exist_ok=True)
    with open(metrics_path, 'w') as outfile:
        json.dump(metrics, outfile)


# Defining and parsing the command-line arguments
def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id', type=str, help="GCP project id")
    parser.add_argument('--feature_path', type=str, help="CSV file with features")
    parser.add_argument('--model_repo', type=str, help="Name of the model bucket")
    parser.add_argument('--metrics_path', type=str, help="Name of the file to be used for saving evaluation metrics")
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    train_mlp(**parse_command_line_arguments())
    # The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions
