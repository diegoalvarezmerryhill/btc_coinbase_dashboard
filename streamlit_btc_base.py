import pandas as pd
import datetime as dt
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

today = dt.date.today()

before = today - dt.timedelta(days= (7 * 365) + 2)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')

tickers = ['^GSPC', 'COIN', 'BTC-USD', 'DOGE-USD']
columns = ['BTC', 'coinbase', 'Dogecoin', 'SPX']

df = yf.download(tickers, start_date, end_date)['Adj Close']
df.columns = columns

st.header("Coinbase - Bitcoin Dashboard")

options = ["coinbase", "BTC", "DOGE"]
sidebar = st.sidebar.selectbox("select security", options)

##############################################################
if sidebar == "coinbase":
    
    st.subheader("Coinbase")
    st.text("Close Price")
    
    #clean data
    coin_data = df['coinbase'].dropna().to_frame()
    st.line_chart(coin_data)
    
    #change index 
    coin_data.index = coin_data.index.strftime("%m/%d/%Y")
    
    coin_data['pct_change'] = coin_data.pct_change().dropna()
    st.line_chart(coin_data['pct_change'])
    st.write(coin_data)
    
    coin_fig, coin_ax = plt.subplots()
    coin_ax.hist(coin_data['pct_change'])
    coin_ax.set_title("daily adjusted close retuns")
    coin_ax.set_xlabel("Percentage Return")
    coin_ax.set_ylabel("Frequency")
    st.pyplot(coin_fig)
    
    st.subheader("In comparison")
    
    coin_pct_chage = coin_data['pct_change'].dropna()
    btc_pct_change = df['BTC'].pct_change().dropna()
    spx_pct_change = df['SPX'].pct_change().dropna()
    
    hist_data = [coin_pct_chage, btc_pct_change, spx_pct_change]
    group_labels = ['Coinbase', 'Bitcoin', 'S&P']
    
    fig = ff.create_distplot(hist_data, group_labels)
    st.plotly_chart(fig, use_container_width=True)
    
    #1 day rolling covariance
    
    st.subheader("1 day rolling covariance with bitcoin")
    coin_btc_one = df['coinbase'].rolling(3).corr(df['BTC'])
    st.line_chart(coin_btc_one)
    
    st.subheader("1 day rolling covariance with S&P")    
    coin_spx_one = df['coinbase'].rolling(3).corr(df['SPX'])
    st.line_chart(coin_spx_one)
    

###############################################################       
if sidebar == "BTC":
    
    st.subheader("BTC")
    st.text("Close Price")
    
    #clean data
    coin_data = df['BTC'].dropna().to_frame()
    st.line_chart(coin_data)
    
    #change index 
    coin_data.index = coin_data.index.strftime("%m/%d/%Y")
    
    coin_data['pct_change'] = coin_data.pct_change().dropna()
    st.line_chart(coin_data['pct_change'])
    st.write(coin_data)
    
    coin_fig, coin_ax = plt.subplots()
    coin_ax.hist(coin_data['pct_change'], bins = 100)
    coin_ax.set_title("daily adjusted close retuns")
    coin_ax.set_xlabel("Percentage Return")
    coin_ax.set_ylabel("Frequency")
    st.pyplot(coin_fig)
    
    st.subheader("In comparison")
    
    coin_pct_chage = coin_data['pct_change'].dropna()
    BTC_pct_change = df['BTC'].pct_change().dropna()
    spx_pct_change = df['SPX'].pct_change().dropna()
    
    hist_data = [coin_pct_chage, BTC_pct_change, spx_pct_change]
    group_labels = ['BTC', 'Bitcoin', 'S&P']
    
    fig = ff.create_distplot(hist_data, group_labels)
    st.plotly_chart(fig, use_container_width=True)
    
    #1 day rolling covariance
    
    st.subheader("3 day rolling covariance with bitcoin")
    coin_BTC_one = df['BTC'].rolling(3).corr(df['coinbase'])
    st.line_chart(coin_BTC_one)
    
    st.subheader("3 day rolling covariance with S&P")    
    coin_spx_one = df['BTC'].rolling(3).corr(df['SPX'])
    st.line_chart(coin_spx_one)
    
###############################################################     
if sidebar == "DOGE":
    
    st.subheader("Dogecoin")
    st.text("Close Price")
    
    #clean data
    coin_data = df['Dogecoin'].dropna().to_frame()
    st.line_chart(coin_data)
    
    #change index 
    coin_data.index = coin_data.index.strftime("%m/%d/%Y")
    
    coin_data['pct_change'] = coin_data.pct_change().dropna()
    st.line_chart(coin_data['pct_change'])
    st.write(coin_data)
    
    coin_fig, coin_ax = plt.subplots()
    coin_ax.hist(coin_data['pct_change'], bins = 100)
    coin_ax.set_title("daily adjusted close retuns")
    coin_ax.set_xlabel("Percentage Return")
    coin_ax.set_ylabel("Frequency")
    st.pyplot(coin_fig)
    
    st.subheader("In comparison")
    
    coin_pct_chage = coin_data['pct_change'].dropna()
    Dogecoin_pct_change = df['Dogecoin'].pct_change().dropna()
    spx_pct_change = df['SPX'].pct_change().dropna()
    
    hist_data = [coin_pct_chage, Dogecoin_pct_change, spx_pct_change]
    group_labels = ['Dogecoin', 'Bitcoin', 'S&P']
    
    fig = ff.create_distplot(hist_data, group_labels)
    st.plotly_chart(fig, use_container_width=True)
    
    #1 day rolling covariance
    
    st.subheader("3 day rolling covariance with bitcoin")
    coin_Dogecoin_one = df['Dogecoin'].rolling(3).corr(df['coinbase'])
    st.line_chart(coin_Dogecoin_one)
    
    st.subheader("3 day rolling covariance with S&P")    
    coin_spx_one = df['Dogecoin'].rolling(3).corr(df['SPX'])
    st.line_chart(coin_spx_one)
    
