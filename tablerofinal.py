import streamlit as st
import pandas as pd
import numpy as np


gastos=pd.read_csv("https://drive.google.com/file/d/1kZOOvLyTGsIqlwiKbbhHpXvtve6MRZBC/view?usp=sharing")
facturacion=pd.read_csv("https://drive.google.com/file/d/1SwjLrbVWycFZXEMI_wfKtMc3ClkuGczf/view?usp=sharing")
saldos=pd.read_csv("https://drive.google.com/file/d/1HCb8XhXbRfqY6ghHwvqFCnEvK9l-i5xX/view?usp=sharing")
clientes=pd.read_csv("https://drive.google.com/file/d/1SwjLrbVWycFZXEMI_wfKtMc3ClkuGczf/view?usp=sharing")
costos=pd.read_csv("https://drive.google.com/file/d/1kZOOvLyTGsIqlwiKbbhHpXvtve6MRZBC/view?usp=sharing")

st.image("https://calorycontrol.com.mx/staging/wp-content/uploads/2021/04/LogoHorizontal-768x210.png", use_column_width=True)

st.markdown("<h1 style='text-align: center; font-weight: bold; color: black; font-size: 48px; font-family: Montserrat;'>Tablero interactivo de desempeño</h1>", unsafe_allow_html=True)
years_to_filter = st.slider('year', 2021, 2023, 2021)
filtered_data = facturacion[facturacion[FECHA_DOC].dt.year == years_to_filter]

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Ingresos</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Costos</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Gastos</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Factores financieros</h1>", unsafe_allow_html=True)

