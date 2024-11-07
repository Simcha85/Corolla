import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title('USED TOYOTA COROLLA PRICES 1998-2004')
st.subheader('Sales Data')
st.image('Toyota.jpg')

data=pd.read_csv('ToyotaCorolla2.csv')
del data['Unnamed: 0']
del data['Unnamed: 0.1']

edited=st.data_editor(data)


models=data['Model'].unique

sales1=data[['Model','Mfg_Year','Price']]

fig=px.scatter(data,x='Fuel_Type',y='HP', color='Price')
st.subheader('Scatter Chart of Fuel Type vs Hoersepower of Vehicles')
st.plotly_chart(fig)

sales2=data[['Fuel_Type','Mfg_Year','Price']]

fig2=px.bar(data,x='Mfg_Year',y='Price',color='Fuel_Type', barmode='group')
st.subheader('Turnover of Sales by Fuel Type USD')
st.plotly_chart(fig2)

fig3=px.histogram(data,x='Price',color='Mfg_Year')
st.subheader('Histogram of Vehicle Price')
st.write('This shows the most common price points along with the manufacturing year of the vehicles')
st.plotly_chart(fig3)
