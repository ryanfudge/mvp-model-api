from pydantic import BaseModel

class PlayerStats(BaseModel):
    vorp: float
    per: float
    ws: float
    ows: float
    dws: float
    pts_per_g: float
    fg_per_g: float