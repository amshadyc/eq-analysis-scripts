import yfinance as yf
import pandas as pd

# Hardcoded Nifty 50 symbols
nifty50_symbols = [
    "ADANIPORTS.NS",
    "APOLLOHOSP.NS",
    "ASIANPAINT.NS",
    "AXISBANK.NS",
    "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS",
    "BAJAJFINSV.NS",
    "BPCL.NS",
    "BHARTIARTL.NS",
    "BRITANNIA.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "DIVISLAB.NS",
    "DRREDDY.NS",
    "EICHERMOT.NS",
    "GRASIM.NS",
    "HCLTECH.NS",
    "HDFCBANK.NS",
    "HDFCLIFE.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HINDUNILVR.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "IOC.NS",
    "ITC.NS",
    "INDUSINDBK.NS",
    "INFY.NS",
    "JSWSTEEL.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "M&M.NS",
    "MARUTI.NS",
    "NTPC.NS",
    "NESTLEIND.NS",
    "ONGC.NS",
    "POWERGRID.NS",
    "RELIANCE.NS",
    "SBILIFE.NS",
    "SHREECEM.NS",
    "SBIN.NS",
    "SUNPHARMA.NS",
    "TCS.NS",
    "TATACONSUM.NS",
    "TATAMOTORS.NS",
    "TATASTEEL.NS",
    "TECHM.NS",
    "TITAN.NS",
    "UPL.NS",
    "ULTRACEMCO.NS",
    "WIPRO.NS",
]

result_df = pd.DataFrame(
    columns=["Symbol", "Diluted EPS", "Current Price", "P/E Ratio"]
)


# Iterate through each symbol and fetch financial data
for symbol in nifty50_symbols:
    ticker = yf.Ticker(symbol)

    # Fetch quarterly financial data
    quarterly_data = ticker.quarterly_financials
    latest_price = ticker.history(period="1d")["Close"].iloc[-1]
    print("Latest Price:", latest_price)
    # print (quarterly_data)
    # Extract only the dates (index) from the DataFrame
    latest_date = quarterly_data.columns.max()
    print(symbol)
    diluted_eps_latest_date = quarterly_data.loc["Diluted EPS", latest_date]
    basic_eps_latest_date = quarterly_data.loc["Basic EPS", latest_date]
    print(f"Diluted EPS : {diluted_eps_latest_date}")
    # print(f"Basic EPS for {latest_date}: {basic_eps_latest_date}")
    pe_ratio = latest_price / diluted_eps_latest_date
    print(f"P/E Ratio: {pe_ratio}", "\n\n")
    temp_df = pd.DataFrame(
        {
            "Symbol": [symbol],
            "Diluted EPS": [diluted_eps_latest_date],
            "Current Price": [latest_price],
            "P/E Ratio": [pe_ratio],
        }
    )

    # Concatenate the temporary DataFrame to the result DataFrame
    result_df = pd.concat([result_df, temp_df], ignore_index=True)

print(result_df)
result_df.to_csv("current_pe_ratio_nifty_50.csv", index=False)
