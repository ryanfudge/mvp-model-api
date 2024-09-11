import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from api.schemas.player_stats import PlayerStats
from scripts.fetch_player_data import fetchToModel


@pytest.fixture
def mock_get_stats():
    with patch('scripts.fetch_player_data.get_stats') as mock:
        advanced_stats = pd.DataFrame({
            'VORP': [5.2],
            'OWS': [4.1],
            'DWS': [2.3],
            'WS': [6.4],
            'PER': [25.6]
        })
        per_game_stats = pd.DataFrame({
            'FG': [8.5],
            'PTS' : [25.0]
        })
        mock.side_effect = [advanced_stats, per_game_stats]
        yield mock

def test_fetch_to_model(mock_get_stats):
    result = fetchToModel("LeBron James")
    
    assert mock_get_stats.call_count == 2
    
    assert isinstance(result, PlayerStats)
    assert result.vorp == 5.2
    assert result.ows == 4.1
    assert result.dws == 2.3
    assert result.ws == 6.4
    assert result.per == 25.6
    assert result.fg_per_g == 8.5
    assert result.pts_per_g == 25.0

def test_fetch_to_model_error_handling():
    with patch('scripts.fetch_player_data.get_stats', side_effect=Exception("API Error")):
        with pytest.raises(Exception, match="API Error"):
            fetchToModel("LeBron James")