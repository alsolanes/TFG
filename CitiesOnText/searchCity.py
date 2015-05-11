def get_db_news():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.noticies
    return db.noticies.find_one()['descripcio']

def get_db_ciutats():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.ciutats
    return db

def get_coords_city(nom):
    db = get_db_ciutats()
    a = db.ciutats.find({"name":nom})
    #a = db.command("text", "ciutats",search=nom, ,limit=10)
    nom.replace(',','')
    nom.split()
    for city in a:
        print city
    return a
def get_common_words():
    from collections import Counter
    import csv
    db = get_db_ciutats()
    paraules = []
    total = db.ciutats.find().count()
    a = db.ciutats.find()
    i = 0
    for ciutat in a:
        i+=1
        if i%1000 == 0: 
            print i/total
        paraula = ciutat['name'].replace(',','')
        for w in paraula:
            paraules.append(w.encode('utf-8'))
    writer = csv.writer(open("common_words.csv",'w'))
    writer.writerows(paraules)
    print 'End'

def get_city():
    print 'Beginning scan...'
    text = get_db_news()
    text = text.split()
    ciutats = []
    for t in text:
        if t[0].isupper():
            ciutats.append(t.replace(',',''))
    similars = []
    for ciutat in ciutats:
        #print ciutat
        similars = get_coords_city(ciutat)
    print 'End Scan'


##########################################################
def get_db_news2():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.noticies
    return db.noticies.find_one()['descripcio']
import nltk
from nltk.corpus import cess_cat
text = get_db_news2()
opt1= 


###########################################################333
#get_city()
#get_common_words()

