import json
import os

import pandas as pd
from flask import Flask, request

from resources import model_trainer

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/training-api/model', methods=['POST'])
def train_models():
    # the training input data in the message body as a JSON payload
    training_input = request.get_json()
    df = pd.read_json(json.dumps(training_input), orient='records')
    resp = model_trainer.train(df.values)
    return resp


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
