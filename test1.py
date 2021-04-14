import pandas as pd
import datetime as dt
import streamlit as st
import pandas_datareader as web
import matplotlib.pyplot as plt

end = dt.datetime.today()
start = end - dt.timedelta(days = (8 * 365) + 2)

#high frequency
high_breakeven =  ['T5YIE','T10YIE']
high_breakeven_columns = ['5y', '10y']

high_breakeven_df = []

for i in enumerate(high_breakeven):
    
    series = web.DataReader(i[1], 'fred', start, end)
    high_breakeven_df.append(series)
    
high_breakeven_df = pd.concat(high_breakeven_df, axis = 1)
high_breakeven_df.columns = high_breakeven_columns

low_breakeven = ['T7YIEM' , 'T20YIEM']
low_breakeven_columns = ['7y', '20y ']

low_breakeven_df = []

for i in enumerate(low_breakeven):
    
    series = web.DataReader(i[1], 'fred', start, end)
    low_breakeven_df.append(series)
    
low_breakeven_df = pd.concat(low_breakeven_df, axis = 1)
low_breakeven_df.columns = low_breakeven_columns

st.header("Breakeven Rates")

st.line_chart(high_breakeven_df)
st.line_chart(low_breakeven_df)