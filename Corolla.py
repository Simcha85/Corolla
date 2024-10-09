import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

data=pd.read_excel('ToyotaCorolla.xls')


st.title('USED TOYOTA COROLLA PRICES')
st.subheader('RAW DATA')
st.write(data)

st.image('Toyota.jpg')

st.selectbox('Model')