import pandas as pd

class DataAnalyze:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def analyze(self) -> None:
        self.df["Power"] = self.df["Voltage"] * self.df["Current"]
        time = pd.to_datetime(self.df['Time'])
        self.df['hour'] = time.dt.hour
        self.df['month'] = time.dt.month
        # return self.df