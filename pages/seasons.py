import streamlit as st
import pandas as pd 
import altair as alt 
import plotly.express as px 
from data_loader import load_teams
from data_processing import teams_to_dataframe, teams_to_dataframe_by_season, dataframe_to_dataframe_dic
from team import Team 

@st.cache_data
def get_teams():
    return load_teams()

teams: Team = get_teams()
df_global: pd.DataFrame = teams_to_dataframe(teams)
df_seasons: pd.DataFrame = teams_to_dataframe_by_season(teams)

numeric_cols = df_seasons.select_dtypes(include='number').columns.drop(['Season'])
team_names = df_global["Team"]
stat = st.selectbox("Select statistic", numeric_cols)
team_name = st.selectbox("Select a team", team_names)

df_filtered = df_seasons[df_seasons["Team"] == team_name]

df_plot = df_filtered.set_index("Season")[stat]

st.line_chart(df_plot)

df_spider: pd.DataFrame = dataframe_to_dataframe_dic(df_global, team_name)

fig = px.line_polar(df_spider, r='r', theta='theta', line_close=True)


fig.update_traces(
    fill="toself",
    hovertemplate="%{theta}<br>%{r:.0%}<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

