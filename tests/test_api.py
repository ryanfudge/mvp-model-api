import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient
from api.main import app  # Ensure this path is correct based on your project structure

@pytest.mark.asyncio
async def test_predict():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Example payload for prediction
        payload = {
            "vorp": 1.2,
            "per": 22.1,
            "ws": 5.6,
            "ows": 3.2,
            "dws": 2.4,
            "pts_per_g": 25.4,
            "fg_per_g": 9.8
        }
        response = await ac.post("/predict", json=payload)
        assert response.status_code == 200
        result = response.json()
        assert "predicted_award_share" in result
        assert isinstance(result["predicted_award_share"], float)
