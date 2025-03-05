#make class PlotGrapg by get a model to predict y is Power in 24hr in a day and x is Dust to plot line graph from google sheets

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ai.LSVM import LSVM
import io
import base64

class PlotPowerGraph:
    def __init__(self, powerModel: LSVM, dustModel: LSVM) -> None:
        self.powerModel = powerModel
        self.dustModel = dustModel
        self.df = self.prepareData()

    def prepareData(self) -> pd.DataFrame:
        df = pd.DataFrame()
        df['hour'] = np.linspace(0, 24, 24)
        df['month'] = pd.Timestamp.now().normalize().month
        df['dust'] = self.dustModel.predict(df)

        # Predict power using the model
        df['power'] = self.powerModel.predict(df)
        return df

    def plot(self) -> None:
        df = self.df
        plt.plot(df['hour'], df['power'], label='Actual Power', color='black')

        # Save the plot to a BytesIO object and encode it as a base64 string
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        return img_base64

