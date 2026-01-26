import streamlit as st
from data_loader import load_teams
from data_processing import teams_to_dataframe, teams_to_dataframe_by_season
import altair as alt

@st.cache_data
def get_teams():
    return load_teams()

teams = get_teams()
df_global = teams_to_dataframe(teams)
df_seasons = teams_to_dataframe_by_season(teams)

st.title("Global stats")

st.dataframe(df_global)
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

numeric_cols = df_seasons.select_dtypes(include='number').columns.drop(['Season'])
stat = st.selectbox("Select statistic", numeric_cols)

chart = alt.Chart(df_seasons).mark_line(point=True).encode(
    x=alt.X('Season:O', title='Season'),   
    y=alt.Y(f'{stat}:Q', title=stat),    
    color='Team:N',                        
    tooltip=['Team', 'Season', stat]      
).interactive()  
st.altair_chart(chart, use_container_width=True)

stat = st.selectbox(
    "Choose a stat",
    df_global.columns.drop("Team")
)

df_sorted = df_global.sort_values(by=stat, ascending=False)

chart = alt.Chart(df_sorted).mark_bar().encode(
    x=alt.X(stat, title=stat),
    y=alt.Y('Team', sort='-x', title='Team')

)
st.altair_chart(chart, use_container_width=True)
