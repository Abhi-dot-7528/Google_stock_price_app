import yfinance as yf
import streamlit as st


st.write("""
# My Stock Price App
""")

tickerSymbol = 'GOOG'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start='2012-4-24', end='2022-4-24')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
