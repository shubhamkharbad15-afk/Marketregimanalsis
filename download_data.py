import yfinance as yf
import pandas as pd

tickers = {
    "SP500": "^GSPC",
    "VIX": "^VIX",
    "AAPL": "AAPL",
    "JPM": "JPM",
    "XOM": "XOM",
    "GLD": "GLD",
    "TLT": "TLT"
}

start_date = "1993-01-01"
end_date = "2024-12-31"

for name, ticker in tickers.items():
    print(f"Downloading {name}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f"{name}.csv")

print("All files downloaded!")