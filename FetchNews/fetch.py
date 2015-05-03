import feedparser
from bs4 import BeautifulSoup
import unidecode
from time import mktime
import time
from datetime import datetime

def get_db_news():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.noticies
    return db

def add_news(db, diari, data, titol, desc):
    db.noticies.insert({"diari":diari, "data":data, "titol":titol, "descripcio":desc})  

def get_news(diari,web, today=False):
    db = get_db_news()
    rss = web
    feed = feedparser.parse(rss)
    print len(feed["entries"])
    vals = []
    for key in feed["entries"]: 
        title = BeautifulSoup(key["title"]).get_text()
        date = datetime.fromtimestamp(mktime(key["published_parsed"]))
        date_formated = date.strftime("%d/%m/%Y")
        if today and date_formated != time.strftime("%d/%m/%Y"):
            print date_formated
            continue
        if db.noticies.find({"titol":title}).count() > 0:
            print title
            continue
        #desc_formated = BeautifulSoup(unidecode.unidecode(key["description"])).get_text()
        desc_formated = BeautifulSoup(key["description"]).get_text()
        #print desc_formated.get_text()
        ret_val = [date_formated,title,desc_formated]
        #print ret_val
        add_news(db,diari,date_formated,title,desc_formated)
        vals.append(ret_val)
    return vals

get_news('ara','http://www.ara.cat/rss/')
get_news('regio7','http://www.regio7.cat/elementosInt/rss/1')
get_news('vilaweb','http://www.vilaweb.cat/rss/')
db = get_db_news()
print db.noticies.find().count()
