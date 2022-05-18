# Day 36: Stock News Monitoring Project

# TODO 3. SEND SMS MESSAGE
import requests

import news
from stock_price import StockPrice
from news import GetNews
from send_sms import SendSMS
stock_price =StockPrice()
stock_close = stock_price.get_close_price()
print(stock_close)

for i in range(50):
    stock_compare = stock_price.compare_price()
    print(stock_compare)
    if stock_compare[0] !=None:
        date = stock_compare[0]
        news = GetNews(date)
        print(f"{news.date} days news is as shown here")
        stock_news =news.get_news()[0]
        content =f"{stock_news[0]}:\n\t{stock_news[1]}"
        subject =f"{date}'s News:"
        print(subject,content)
        print("*********")
        send_sms = SendSMS(content)

