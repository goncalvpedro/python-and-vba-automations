import pandas as pd
import json

class Portfolio:
    portfolio = []

    def __init__(self, filepath):
        self.filepath = filepath

    def add_to_portfolio(self, ticker,  paid_price, active, quantity = 0, buying_date = ''):
        asset = {}
        self.asset['ticker'] = ticker
        self.asset['paid_price'] = paid_price
        self.asset['buying_date'] = buying_date
        self.asset['quantity'] = quantity
        self.asset['active'] = active

        self.portfolio.append(asset)

        return self.portfolio


    def read_json(self):
        with open(self.filepath, 'rb') as file:
            data = json.load(file)
        self.portfolio = data
        return self.portfolio 
    
    
    def dump_json(self):
        with open('data/portfolio.json', 'w') as file:
            json.dump(self.portfolio, file, ensure_ascii=False, indent=2)
    

filepath = 'data/portfolio.json'

data = Portfolio(filepath).read_json()

print(data)