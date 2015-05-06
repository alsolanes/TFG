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
get_city()
