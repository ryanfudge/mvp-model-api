import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from api.schemas.player_stats import PlayerStats
from scripts.fetch_player_data import fetchToModel  

@pytest.fixture
def mock_get_stats():
    with patch('scripts.fetch_to_model.get_stats') as mock:
        advanced_stats = pd.DataFrame({
            'VORP': [5.2],
            'OWS': [4.1],
            'DWS': [2.3],
            'WS': [6.4],
            'PER': [25.6]
        })
        per_game_stats = pd.DataFrame({
            'FG': [8.5]
        })
        mock.side_effect = [advanced_stats, per_game_stats]
        yield mock

@pytest.fixture
def mock_predict_mvp():
    with patch('scripts.fetch_to_model.predict_mvp') as mock:
        mock.return_value = {"mvp_award_share_prediction": 0.75}
        yield mock

def test_fetch_to_model(mock_get_stats, mock_predict_mvp):
    result = fetchToModel("LeBron James")
    
    assert mock_get_stats.call_count == 2
    
    called_stats = mock_predict_mvp.call_args[0][0]
    assert isinstance(called_stats, PlayerStats)
    assert called_stats.vorp == 5.2
    assert called_stats.ows == 4.1
    assert called_stats.dws == 2.3
    assert called_stats.ws == 6.4
    assert called_stats.per == 25.6
    assert called_stats.fg_per_g == 8.5
    
    assert result == {"mvp_award_share_prediction": 0.75}

def test_fetch_to_model_error_handling():
    with patch('scripts.fetch_to_model.get_stats', side_effect=Exception("API Error")):
        with pytest.raises(Exception, match="API Error"):
            fetchToModel("LeBron James")