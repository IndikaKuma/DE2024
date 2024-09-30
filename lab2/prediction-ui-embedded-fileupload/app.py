# importing Flask and other modules
import os
from pathlib import Path

import pandas as pd
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

from diabetes_predictor import DiabetesPredictor

# Flask constructor
app = Flask(__name__)

dp = DiabetesPredictor(os.environ.get('MODEL_NAME', 'MODEL_NAME environment variable is not set.'))


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkdiabetes', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        # we are going to save the file locally at a folder. if the folder does not exist, we need to create it
        home = str(Path.home())
        service_home = os.path.join(home, ".service")
        if not os.path.exists(service_home):
            os.makedirs(service_home)
        # pfile is the name we used in the user_form.html
        if 'pfile' not in request.files:
            return jsonify({'message': 'No file part in the request'}, sort_keys=False, indent=4), 400

        file = request.files['pfile']

        if file.filename == '':
            return jsonify({'message': 'No file selected for uploading'}, sort_keys=False, indent=4), 400
        else:
            # save the uploaded file locally (at the server side)
            filename = secure_filename(file.filename)
            file_path = os.path.join(service_home, filename)
            file.save(file_path)
            # make predictions
            df = pd.read_json(file_path)
            status = dp.predict_single_record(df)
            # clean up - remove the downloaded file
            try:
                os.remove(file_path)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)

            return render_template("response_page.html",
                                   prediction_variable=status[0])

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
