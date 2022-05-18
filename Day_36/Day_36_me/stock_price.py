import requests
# TODO 1. EXTRACT THE STOCK PRICE
# Alpha Vantage API DOCUMENATION
stock_url ="https://www.alphavantage.co/query?"
stock_api_key ="HOWSBGGPFW5WX7TC"
stock_param={
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "outputsize":"compact",
    "apikey": stock_api_key,
}

class StockPrice:
    def __init__(self):
        self.stock_res =requests.get(url=stock_url,params=stock_param)
        self.stock_res.raise_for_status()
        self.stock_data = self.stock_res.json()["Time Series (Daily)"]
        self.stock_close =[(key,item['4. close']) for (key,item) in self.stock_data.items()]
        self.st_date =0
        self.benchmark = 0.05

    def get_close_price(self):
        return self.stock_close

    def compare_price(self):
        now =self.stock_close[self.st_date][1]
        previous = self.stock_close[self.st_date+1][1]
        percent = round((float(now)- float(previous))/float(previous),3)
        if abs(percent) > self.benchmark:
            excess_date= self.stock_close[self.st_date][0]
            self.st_date += 1
            return (excess_date,percent)
        else:
            self.st_date += 1
            return (None,percent)





