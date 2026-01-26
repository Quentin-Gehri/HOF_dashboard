import streamlit as st
import reading_data
from team import Team

@st.cache_data
def load_teams() -> list[Team]:
    return reading_data.reading_data()
