import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

gastos=pd.read_csv("https://drive.google.com/file/d/1kZOOvLyTGsIqlwiKbbhHpXvtve6MRZBC/view?usp=sharing")
facturacion=pd.read_csv("https://drive.google.com/file/d/1SwjLrbVWycFZXEMI_wfKtMc3ClkuGczf/view?usp=sharing")


st.image("https://calorycontrol.com.mx/staging/wp-content/uploads/2021/04/LogoHorizontal-768x210.png", use_column_width=True)

st.markdown("<h1 style='text-align: center; font-weight: bold; color: black; font-size: 48px; font-family: Montserrat;'>Tablero interactivo de desempeño</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Ingresos</h1>", unsafe_allow_html=True)

facturacion = facturacion[facturacion['STATUS']!='C']

facturacion['FECHA'] = pd.to_datetime(facturacion['FECHA'])
facturacion['Mes'] = facturacion['FECHA'].dt.month
facturacion['Año'] = facturacion['FECHA'].dt.year
facturacion[['Mes', 'Año', 'CVE_VEND']] = facturacion[['Mes', 'Año','CVE_VEND']].astype(str)
facturacion['Año_Mes'] = facturacion['Año'] + facturacion['Mes'] + facturacion['CVE_VEND']
group_facturacion = facturacion.groupby(['SERIE', 'Año_Mes', 'Año', 'Mes', 'CVE_VEND']).sum()
group_facturacion = group_facturacion.reset_index()
group_facturacion.SERIE.unique()
DEV =  group_facturacion[group_facturacion['SERIE']== 'DEV']
F = group_facturacion[group_facturacion['SERIE']== 'F']
NC = group_facturacion[group_facturacion['SERIE']== 'NC']
NC_F = pd.merge(DEV,NC, on ='Año_Mes',how= 'outer')
facturacion_N = pd.merge(NC_F,F, on ='Año_Mes',how= 'outer')
facturacion_N = facturacion_N.drop(['Año_x', 'Mes_x', 'CVE_VEND_x', 'DES_FIN_x', 'SERIE_x', 
                                    'DESCUENTO_x', 'SERIE_y', 'Año_y', 'Mes_y', 'CVE_VEND_y',
                                    'DESCUENTO_y', 'DES_FIN_y', 'SERIE','DES_FIN'], axis=1)
facturacion_N = facturacion_N.rename(columns ={ 'CAN_TOT_x': 'Devoluciones', 'CAN_TOT_y':'Notas_Credito', 'CAN_TOT':'Facturacion'})
facturacion_N.loc[22]=['2020128.0', 6987.500,0,2020,12,'8.0',0,0]
facturacion_N.loc[48]=['202098.0', 9508.983,0,2020,9,'8.0',0,0]
facturacion_N.loc[80]=['2022103.0', 70000.000	,0,2022,10,'3.0',0,0]
facturacion_N.loc[121]=['20201212.0', 0,30172.40,2020,12,'12.0',0,0]
facturacion_N.loc[130]=['202097.0', 0,2575.40,2020,9,'7.0',0,0]
facturacion_N.loc[133]=['2021125.0', 0,1714.55,2021,12,'5.0',0,0]
facturacion_N.loc[136]=['202123.0', 0,9965.00,2021,2,'3.0',0,0]
facturacion_N.loc[137]=['202128.0', 0,7250.00,2021,2,'8.0',0,0]
facturacion_N.loc[144]=['202158.0', 0,25438.00,2021,5,'8.0',0,0]
facturacion_N = facturacion_N.fillna(0)
facturacion_N[['Mes', 'Año']] = facturacion_N[['Mes', 'Año']].astype(float)
facturacion_N['Ventas_Netas'] = facturacion_N['Facturacion']-facturacion_N['DESCUENTO']-facturacion_N['Notas_Credito']-facturacion_N['Devoluciones']
facturacion_N.isnull().sum()

facturacion_N = facturacion_N.reindex(columns=['Año_Mes','Año','Mes','CVE_VEND','Facturacion','Devoluciones',
                               'Notas_Credito','DESCUENTO', 'Ventas_Netas'])
DEV =  facturacion_N.drop(['Año_Mes','Notas_Credito','Facturacion','DESCUENTO','Ventas_Netas'], axis =1)
DEV['Serie'] = 'Devoluciones'
DEV = DEV.rename(columns={'Devoluciones': 'Monto'})

F = facturacion_N.drop(['Año_Mes','Notas_Credito','Devoluciones','DESCUENTO','Ventas_Netas'], axis =1)
F['Serie'] = 'Ventas Brutas'
F = F.rename(columns={'Facturacion': 'Monto'})

NC = facturacion_N.drop(['Año_Mes','Facturacion','Devoluciones','DESCUENTO','Ventas_Netas'], axis =1)
NC['Serie'] = 'Notas de Crédito'
NC = NC.rename(columns={'Notas_Credito': 'Monto'})

DES = facturacion_N.drop(['Año_Mes','Notas_Credito','Devoluciones','Facturacion','Ventas_Netas'], axis =1)
DES['Serie'] = 'Descuentos'
DES = DES.rename(columns={'DESCUENTO': 'Monto'})

F_NET = facturacion_N.drop(['Año_Mes','Notas_Credito','Devoluciones','Facturacion','DESCUENTO'], axis =1)
F_NET['Serie'] = 'Ventas Netas'
F_NET = F_NET.rename(columns={'Ventas_Netas': 'Monto'})

facturacion_Conc = pd.concat([F_NET, NC, DES, DEV]) 

F_NET_Grup = F_NET.groupby(['Año','CVE_VEND']).sum()
F_NET_Grup = F_NET_Grup.reset_index()

graf3 = alt.Chart(DEV).mark_arc().encode(
    theta=alt.Theta(field='Monto', type='quantitative', title='Devoluciones'),
    color=alt.Color(field='CVE_VEND', type='nominal', title='Vendedor', scale=alt.Scale(scheme='redgrey')),
    tooltip=['Año','Mes', 'Monto', 'Serie', 'CVE_VEND']
).properties(
    title=alt.TitleParams(
        text='Devoluciones',
        fontSize=14,
        font='Arial',
        fontWeight='bold'
    )
).transform_filter(
    click
)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Costos</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Gastos</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black; font-size: 24px; font-family: Montserrat;'>Factores financieros</h1>", unsafe_allow_html=True)

