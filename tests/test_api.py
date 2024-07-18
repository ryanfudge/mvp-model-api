import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient, ASGITransport
from api.main import app

@pytest.mark.asyncio
async def test_predict():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Example payload for prediction
        payload = {
            "vorp": 6.4,
            "per": 31.4,
            "ws": 12.3,
            "ows": 8.4,
            "dws": 3.9,
            "pts_per_g": 33.1,
            "fg_per_g": 11.0
        }
        response = await ac.post("/predict", json=payload)
        assert response.status_code == 200
        result = response.json()
        assert "mvp_award_share_prediction" in result
        assert isinstance(result["mvp_award_share_prediction"], float)
        print(result['mvp_award_share_prediction'])
