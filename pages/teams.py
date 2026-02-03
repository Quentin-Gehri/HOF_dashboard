import streamlit as st
import pandas as pd
import altair as alt
from team import Team
from data_loader import load_teams
from data_processing import teams_to_dataframe, teams_to_dataframe_by_season

@st.cache_data
def get_teams():
    return load_teams()

teams: list[Team] = get_teams()

df_global: pd.DataFrame = teams_to_dataframe(teams)
df_seasons: pd.DataFrame = teams_to_dataframe_by_season(teams)


st.title("Team Statistics Dashboard")

st.header("Global stats")
st.dataframe(df_global)

st.subheader("Global comparisons")

st.scatter_chart(
    data=df_global,
    x="Overall Winrate",
    y="PPG",
    color="Team",
    width=700,
    height=400
)

st.scatter_chart(
    data=df_global,
    x="Overall Winrate",
    y="Conference Winrate",
    color="Team",
    width=700,
    height=400
)

st.header("Stats by season")

numeric_cols = df_seasons.select_dtypes(include="number").columns.drop("Season")

stat_season = st.selectbox(
    "Select statistic (by season)",
    numeric_cols
)

teams_selected = st.multiselect(
    "Select teams",
    df_global["Team"],
    default=df_global["Team"][:5]
)

df_line = (
    df_seasons[df_seasons["Team"].isin(teams_selected)]
    .pivot(index="Season", columns="Team", values=stat_season)
)

st.line_chart(df_line)

st.header("Global ranking")

stat_rank = st.selectbox(
    "Choose a stat for ranking",
    df_global.columns.drop("Team")
)

df_bar = (
    df_global
    .sort_values(by=stat_rank, ascending=False)
)

chart = alt.Chart(df_bar).mark_bar().encode(
    x=alt.X(stat_rank, title=stat_rank),
    y=alt.Y('Team:N', sort='-x', title='Team'),
    tooltip=['Team', stat_rank]
)

st.altair_chart(chart, use_container_width=True)

