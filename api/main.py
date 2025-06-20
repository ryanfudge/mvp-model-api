from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np

from .models.mvp_model import mvp_model
from .schemas.player_stats import PlayerStats

### WILL BE USING https://github.com/swar/nba_api/ FOR POSTGAME DATA RETREIVAL ###

@asynccontextmanager
async def lifespan(app: FastAPI):
    from .scheduler import start_scheduler
    start_scheduler()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/predict")
def predict_mvp(player_stats: PlayerStats):
    data = np.array([[player_stats.vorp, player_stats.per, player_stats.ws, 
                      player_stats.ows, player_stats.dws, player_stats.pts_per_g, 
                      player_stats.fg_per_g]])
    prediction = mvp_model.predict(data)
    return {"mvp_award_share_prediction": prediction[0]}