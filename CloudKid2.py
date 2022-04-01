import streamlit as st
import pandas as pd

st.title("Mi primer app")
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

st.write(df)

st.map(df)

#st.button("Dale click")
#st.button("CORRIDOS TUMBADOS")
