import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv(r'c:\Users\scman\Downloads\ToyotaCorolla.csv')


st.title('USED TOYOTA COROLLA PRICES')
st.subheader('RAW DATA')
st.write(data)

models=data['Model'].unique

st.image('Toyota.jpg')

sales1=data[['Model','Mfg_Year','Price']]

fig=px.scatter(sales1,x='Mfg_Year',y='Price',color='Model')
st.write(fig)

sales2=data[['Fuel_Type','Mfg_Year','Price']]

fig2=px.scatter_3d(sales2,x='Mfg_Year',y='Price',z='Fuel_Type',color='Price')
st.write(fig2)
