import yfinance as yf

ticker = yf.Ticker("IRDM11.SA")

print(ticker.info, sep="\n")