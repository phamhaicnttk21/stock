import yfinance as yf
import pandas as pd
import streamlit as st

st.write("Closing price and volume of Ford")
tickersymbol = 'F'
tickerData = yf.Ticker(tickersymbol)
tickerDF=tickerData.history(period='1d',start='2020-1-1',end='2024-1-6')
st.write("Close price")
st.line_chart(tickerDF.Close)
st.write("Volume")
st.line_chart(tickerDF.Volume)
