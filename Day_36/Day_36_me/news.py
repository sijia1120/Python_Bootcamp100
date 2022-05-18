# TODO 2. EXTRACT THE RELAVENT NEWS
# NewsAPI: News API is a simple HTTP REST API for searching and retrieving live articles from all over the web.
import requests
news_api_key ="5df4804e7a1d40ed937fd172ad635212"
news_url ="https://newsapi.org/v2/everything?"
news_param ={
    "q":"Tesla",
    "from":"2022-05-17",
    "sortBy":"popularity",
    "apiKey":news_api_key,
}

class GetNews:
    def __init__(self,date):
        self.date = date
        self.news_param ={
            "q":"tesla",
            "from":self.date,
            "sortBy":"popularity",
            "apiKey":news_api_key,
        }
        self.news_res = requests.get(url=news_url,params=news_param)
        self.news_res.raise_for_status()
        self.news_data = self.news_res.json()["articles"]
        self.news_dict=[]

    def get_news(self):
        for item in self.news_data:
            self.news_dict.append((item["title"],item["description"]))
            return self.news_dict

