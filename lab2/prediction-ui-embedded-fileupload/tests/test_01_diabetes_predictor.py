import os

import pandas as pd

# content of test_class.py
import diabetes_predictor


class TestDiabetesPredictor:
    def test_predict_single_record(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_data_file = os.path.join(test_dir, "../testResources/prediction_request.json")
        test_model_file = os.path.join(test_dir, "../testResources/model.h5")
        with open(test_data_file) as json_file:
            data = pd.read_json(json_file)
        dp = diabetes_predictor.DiabetesPredictor(model_file=test_model_file)
        status = dp.predict_single_record(data)
        print(os.getcwd())
        assert bool(status[0]) is not None
        assert bool(status[0]) is False
