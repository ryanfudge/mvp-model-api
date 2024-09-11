from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import pytz


# Function to fetch player data and run the model
def scheduled_job():
    from scripts.fetch_player_data import fetchToModel
    print(f"Fetching player data at {datetime.now()}")
    # Example player names; modify this as needed
    player_names = ['Stephen Curry', 'Nikola Jokic', 'Victor Wembanyama', 'Shai Gilgeous-Alexander',
                    'Joel Embiid', 'Luka Doncic', 'Giannis Antetokounmpo', 'Jayson Tatum', 'Domantas Sabonis',
                    'Devin Booker', 'Jalen Brunson', 'Anthony Davis']
    statslist = []
    for name in player_names:
        stats = fetchToModel(name)
        statslist.append({"name": name, "stats": stats})
    return statslist

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=pytz.timezone('US/Eastern'))
    trigger = CronTrigger(hour=2, minute=0)  # Schedule to run every day at 2 AM ET
    scheduler.add_job(scheduled_job, trigger)
    scheduler.start()
