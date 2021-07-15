import os

import xgboost as xgb
from fastapi import FastAPI

from app.model import TelcoData
from app.process import process_request

model_config_folder = os.path.abspath(os.path.dirname(__file__))
model_config_path = os.path.join(model_config_folder, 'model.json')

app = FastAPI()

model = xgb.XGBClassifier()
model.load_model(model_config_path)

@app.post('/')
async def get_churn(request: TelcoData):
    telco_data = request.dict()
    df = process_request(telco_data)
    pred = model.predict(df)
    result = pred.tolist()
    return {"churn": result[0]}
