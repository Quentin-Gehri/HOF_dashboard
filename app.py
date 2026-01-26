import streamlit as st
import pandas as pd
import numpy as np
from geopy import geocoders

from season import Season 
from team import Team
import reading_data

@st.cache_data
def get_data() -> list[Team]:
    return reading_data.reading_data()

teams: list[Team] = get_data()

data = []

for team in teams:
    data.append({
        "Team": team.name,
        "Overall Wins": team.ovr_win,
        "Overall Losses": team.ovr_loss,
        "PPG": round(team.ppg,2),
    })

df = pd.DataFrame(data)

st.title('HOF Teams Stats')
st.dataframe(df)
stat = st.selectbox(
    "Choose a stat",
    ["PPG", "Overall Wins", "Overall Losses"]
)

st.bar_chart(
    df,
    x="Team",
    y=stat
)

gn = geocoders.gege