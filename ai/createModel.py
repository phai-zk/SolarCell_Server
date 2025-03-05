import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor

from ai.dataAnalyze import DataAnalyze

class CreatePredictPowerModel:
    def __init__(self, data_url: str) -> None:
        self.df = pd.read_csv(data_url)
        self.data_analyzer = DataAnalyze(self.df)
        self.data_analyzer.analyze()

    def create(self, fileName = "model") -> None:
        features = ['Dust', 'hour', 'month']
        target = "Power"
        X = self.df[features].values
        y = self.df[target].values

        model = RandomForestRegressor(n_estimators=100)
        model.fit(X, y)

        joblib.dump(model, f"{fileName}.joblib")

class CreatePredictDustModel:
    def __init__(self, data_url: str) -> None:
        self.df = pd.read_csv(data_url)
        self.data_analyzer = DataAnalyze(self.df)
        self.data_analyzer.analyze()

    def create(self, fileName = "model") -> None:
        features = ['hour', 'month']
        target = "Dust"
        X = self.df[features].values
        y = self.df[target].values

        model = RandomForestRegressor(n_estimators=100)
        model.fit(X, y)

        joblib.dump(model, f"{fileName}.joblib")
