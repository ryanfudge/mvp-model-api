import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from basketball_reference_scraper.players import get_stats
import pandas as pd
from api.schemas.player_stats import PlayerStats

def fetchToModel(name):
    df = get_stats(name, stat_type='ADVANCED', playoffs=False, career=False)
    df2 = get_stats(name, stat_type='PER_GAME', playoffs=False, career=False)
    df = df.tail(1)
    df2 = df2.tail(1)
    stats = PlayerStats(
        vorp = df.at[0, 'VORP'],
        ows = df.at[0, 'OWS'],
        dws = df.at[0, 'DWS'],
        ws = df.at[0,'WS'],
        per = df.at[0, 'PER'],
        pts_per_g = df.at[0, 'PPG'],
        fg_per_g = df2.at[0,'FG']
    )
    return stats