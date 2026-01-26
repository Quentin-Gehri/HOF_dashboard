import streamlit as st
from data_loader import load_teams
from data_processing import teams_to_dataframe
import altair as alt

@st.cache_data
def get_teams():
    return load_teams()

teams = get_teams()
df = teams_to_dataframe(teams)

st.title("Global stats")

st.dataframe(df)
stat = st.selectbox(
    "Choose a stat",
    df.columns.drop("Team")
)

df_sorted = df.sort_values(by=stat, ascending=False)

chart = alt.Chart(df_sorted).mark_bar().encode(
    x=alt.X(stat, title=stat),
    y=alt.Y('Team', sort='-x', title='Team')
)

st.altair_chart(chart, use_container_width=True)