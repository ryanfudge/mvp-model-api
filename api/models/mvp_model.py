import joblib
import os

# Path to the model file
model_path = os.path.join(os.path.dirname(__file__), '../../models/nba_mvp_model.joblib')

# Load the model
mvp_model = joblib.load(model_path)