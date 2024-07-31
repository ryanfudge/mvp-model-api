from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np

from scheduler import start_scheduler
from .models.mvp_model import mvp_model
from .schemas.player_stats import PlayerStats

### WILL BE USING https://github.com/swar/nba_api/ FOR POSTGAME DATA RETREIVAL ###

app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_scheduler()

@app.post("/predict")
def predict_mvp(player_stats: PlayerStats):
    data = np.array([[player_stats.vorp, player_stats.per, player_stats.ws, 
                      player_stats.ows, player_stats.dws, player_stats.pts_per_g, 
                      player_stats.fg_per_g]])
    prediction = mvp_model.predict(data)
    return {"mvp_award_share_prediction": prediction[0]}