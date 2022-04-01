import streamlit as st
import pandas as pd

st.title("Mi primer app")
click=st.button("dale click")
srt.write("el valor de click es: ",click)

if click==True:
  st.image("Perrillo.jpg")

#st.markdown(" #titulo ")
#st.markdown(" **este es una vineta** ")

#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
#st.write(df)
#st.map(df)

#st.button("Dale click")
#st.button("CORRIDOS TUMBADOS")
