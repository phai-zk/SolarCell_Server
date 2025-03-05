from ai.createModel import CreatePredictDustModel
from ai.createModel import CreatePredictPowerModel

SPREADSHEET_ID = "1hK_elq8Kv2ovOFghRT6_OAQ0d78GbPGnoKIocPIswHI"
SHEET_NAME = "DataC"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

CreatePredictDustModel(CSV_URL).create("dustModel")
CreatePredictPowerModel(CSV_URL).create("powerModel")