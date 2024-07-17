import pytest
import joblib
import os
import numpy as np

@pytest.fixture
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'nba_mvp_model.joblib')
    model = joblib.load(model_path)
    return model

def test_model_prediction(load_model):
    model = load_model
    # Example feature input for prediction
    input_features = np.array([[1.2, 22.1, 5.6, 3.2, 2.4, 25.4, 9.8]])
    prediction = model.predict(input_features)
    assert prediction.shape == (1,)
    assert isinstance(prediction[0], float)