import joblib

def load_model():
    return joblib.load("models/nba_mvp_model.joblib")

def predict(model, player_stats):
    input_data = [[
        player_stats.vorp,
        player_stats.per,       
        player_stats.ws,
        player_stats.ows,
        player_stats.dws,
        player_stats.pts_per_g,
        player_stats.fg_per_g
    ]]
    return model.predict(input_data)[0]