import streamlit as st
import pandas as pd
import numpy as np

st.header(':grey[Calor y Control] :gear:')
df=pd.read_csv("https://drive.google.com/file/d/11oLcKiW8SgCOp3tGiQCYuRG7pLL_J-Zf/view?usp=share_link/Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown("The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.")

mapa=pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
mapa=mapa.dropna()
st.map(mapa)

st.write(f'Total Records: {len(df)}')
