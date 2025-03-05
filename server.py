from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai.plotPowerGraph import PlotPowerGraph
from ai.LSVM import LSVM
import pandas as pd
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SPREADSHEET_ID = "1hK_elq8Kv2ovOFghRT6_OAQ0d78GbPGnoKIocPIswHI"
SHEET_NAME = "DataC"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


@app.get("/plot_power")
def plot_power():
	model = [LSVM("powerModel.joblib"), LSVM("dustModel.joblib")]
	graphIMG = PlotPowerGraph(model[0], model[1]).plot()
	return {"graph": graphIMG}

@app.get("/predict_power")
def predict_power():
	model = [LSVM("powerModel.joblib"), LSVM("dustModel.joblib")]
	df = pd.DataFrame()
	df['hour'] = [datetime.now().hour]
	df['month'] = pd.Timestamp.now().normalize().month
	df['dust'] = model[1].predict(df)

	predict = model[0].predict(df)
	return {"predict_power": predict}