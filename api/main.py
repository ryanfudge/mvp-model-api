from fastapi import FastAPI
from api.models.mvp_model import load_model, predict
from api.schemas.player_stats import PlayerStats

app = FastAPI

model=load_model()

