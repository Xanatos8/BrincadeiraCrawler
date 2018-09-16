import requests as r
from bs4 import BeautifulSoup as bs
from collections import defaultdict
from pymongo import MongoClient

Client = MongoClient()
db = Client["Crawled"]
crawled = db["Crawled"]
article = db["Articles"]
info = {}
info = ["Link"]
info = ["Content"]
article = {}
article = ["Link"]
article = ["Content"]
principal = "https://www.reuters.com"
extra = "/finance"
article = "/article"


def request(link, extra_rest):
    all_to_visit = []
    new_to_visit = []
    desire = []
    response = r.get(link+extra_rest)
    soup = bs(response.content)
    for link in soup.find_all('a'):
        all_to_visit.append(link.get('href'))
    for page in all_to_visit:
        if page.startswith(extra):
            new_to_visit.append(page)
        if page.startswith(article):
            desire.append(page)
    print(new_to_visit)
    return new_to_visit, desire, soup


def run(principal_link, extra_link):
    d = defaultdict(list)
    visited = []
    to_visit, desire, content = request(principal_link, extra_link)
    visited.append(principal_link+extra_link)
    d[principal_link+extra_link].append(content)


run(principal, extra)
