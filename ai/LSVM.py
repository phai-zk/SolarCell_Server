import joblib
from pandas import DataFrame
import numpy as np

class LSVM:
    def __init__(self, model_path: str) -> None:
        try:
            self.model = joblib.load(model_path)
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

    def predict(self, X: DataFrame):
        predictions = self.model.predict(X)
        predictions  = [f"{pred:.2f}" for pred in predictions]
        return predictions
