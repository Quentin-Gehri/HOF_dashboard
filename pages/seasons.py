import streamlit as st
import pandas as pd
import altair as alt
from data_loader import load_teams
from data_processing import teams_to_dataframe_by_season

# Charger les données
@st.cache_data
def get_teams():
    return load_teams()

teams = get_teams()
df = teams_to_dataframe_by_season(teams)

st.title("Stats per Season (All Teams)")

# Choisir la stat à afficher
numeric_cols = df.select_dtypes(include='number').columns.drop(['Season'])
stat = st.selectbox("Select statistic", numeric_cols)

# Graphique Altair : une ligne par équipe
chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Season:O', title='Season'),   # Ordinal pour saison
    y=alt.Y(f'{stat}:Q', title=stat),     # Quantitative
    color='Team:N',                        # Couleur par équipe
    tooltip=['Team', 'Season', stat]       # Affichage au survol
).interactive()  # permet zoom et pan

st.altair_chart(chart, use_container_width=True)
