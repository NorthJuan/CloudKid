import streamlit as st
import pandas as pd

st.title("Mi primer app")
click=st.button("dale click")
st.write("el valor de click es: ",click)

if click==True:
  st.image("Perrillo.jpg")

#st.markdown(" #titulo ")
#st.markdown(" **este es una vineta** ")
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
#st.write(df)
#st.map(df)
#st.button("Dale click")
#st.button("CORRIDOS TUMBADOS")

num1 = st.slider('Elige el numero 1', 0.0, 100, 25.0)
num2 = st.slider('Elige el numero 2', 0.0, 100, 25.0)
suma = num1+num2
st.write("La suma de", num1," y ", num2,"es :", suma)
