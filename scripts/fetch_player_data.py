from basketball_reference_scraper.players import get_stats

s = get_stats('Stephen Curry', stat_type='ADVANCED', playoffs=False, career=False,)
print(s)