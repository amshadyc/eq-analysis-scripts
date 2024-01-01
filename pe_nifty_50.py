import yfinance as yf
import pandas as pd

# Hardcoded Nifty 50 symbols
nifty50_symbols = [
    "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS", "ICICIBANK.NS",
    "WIPRO.NS", "ONGC.NS", "LT.NS", "ITC.NS", "SBIN.NS", "HDFCBANK.NS", "KOTAKBANK.NS",
    "AXISBANK.NS", "IOC.NS", "NTPC.NS", "SUNPHARMA.NS", "BHARTIARTL.NS", "MARUTI.NS",
    "HCLTECH.NS", "COALINDIA.NS", "BAJAJFINSV.NS", "BAJFINANCE.NS", "ULTRACEMCO.NS",
    "BHARTIARTL.NS", "NESTLEIND.NS", "INDUSINDBK.NS", "HINDALCO.NS", "DRREDDY.NS",
    "POWERGRID.NS", "M&M.NS", "GRASIM.NS", "HEROMOTOCO.NS", "SHREECEM.NS", "CIPLA.NS",
    "NESTLEIND.NS", "TECHM.NS", "ASIANPAINT.NS", "TITAN.NS", "HINDUNILVR.NS",
    "BAJAJ-AUTO.NS", "JSWSTEEL.NS", "TATASTEEL.NS", "UPL.NS", "HINDPETRO.NS",
    "ADANIPORTS.NS", "BAJAJ-AUTO.NS", "BPCL.NS", "DIVISLAB.NS", "TATAMOTORS.NS"
    # Add the remaining Nifty 50 symbols here
]

result_df = pd.DataFrame(columns=["Symbol", "Diluted EPS", "Current Price", "P/E Ratio"])


# Iterate through each symbol and fetch financial data
for symbol in nifty50_symbols:
  ticker = yf.Ticker(symbol)

  # Fetch quarterly financial data
  quarterly_data = ticker.quarterly_financials
  latest_price = ticker.history(period='1d')['Close'].iloc[-1]
  print("Latest Price:",latest_price)
  # print (quarterly_data)
  # Extract only the dates (index) from the DataFrame
  latest_date = quarterly_data.columns.max()
  print(symbol)
  diluted_eps_latest_date = quarterly_data.loc["Diluted EPS", latest_date]
  basic_eps_latest_date = quarterly_data.loc["Basic EPS", latest_date]
  print(f"Diluted EPS : {diluted_eps_latest_date}")
  # print(f"Basic EPS for {latest_date}: {basic_eps_latest_date}")
  pe_ratio = latest_price / diluted_eps_latest_date
  print(f"P/E Ratio: {pe_ratio}","\n\n")
  temp_df = pd.DataFrame({
        "Symbol": [symbol],
        "Diluted EPS": [diluted_eps_latest_date],
        "Current Price": [latest_price],
        "P/E Ratio": [pe_ratio]
    })

  # Concatenate the temporary DataFrame to the result DataFrame
  result_df = pd.concat([result_df, temp_df], ignore_index=True)

print(result_df)
result_df.to_csv('nifty50_pe_results.csv', index=False)