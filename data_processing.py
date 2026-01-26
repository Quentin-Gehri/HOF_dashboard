import pandas as pd
from team import Team
from season import Season
from geopy.geocoders import Nominatim 
from geopy.extra.rate_limiter import RateLimiter

def teams_to_dataframe(teams: list[Team]) -> pd.DataFrame:
    return pd.DataFrame([
        {
            "Team": t.name,
            "Overall Wins": t.ovr_win,
            "Overall Losses": t.ovr_loss,
            "Conference Wins": t.conf_win,
            "Conference Losses": t.conf_loss,
            "Overall Winrate": round(t.ovr_win / (t.ovr_loss+t.ovr_win),2),
            "Conference Winrate": round(t.conf_win / (t.conf_loss+t.conf_win) if (t.conf_loss+t.conf_win) != 0 else 0,2) ,
            "PPG": round(t.ppg, 2),
        }
        for t in teams
    ])

def teams_to_dataframe_by_season(teams: list[Team]) -> pd.DataFrame:
    rows = []
    for t in teams:
        for s in t.seasons:
            rows.append({
                "Team": t.name,
                "Season": s.season_num,
                "Overall Wins": s.ovr_win,
                "Overall Losses": s.ovr_loss,
                "Conference Wins": s.conf_win,
                "Conference Losses": s.conf_loss,
                "Overall Winrate": round(s.ovr_win / (s.ovr_loss+s.ovr_win),2),
                "Conference Winrate": round(s.conf_win / (s.conf_loss+s.conf_win) if (s.conf_loss+s.conf_win) != 0 else 0,2) ,
                "PPG": round(s.ppg, 2),
            })
    return pd.DataFrame(rows)
