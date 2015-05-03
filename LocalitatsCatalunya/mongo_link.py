#database at /var/lib/mongodb/
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.ciutats
    return db
def get_db_news():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.noticies
    return db

def get_db_ciutats():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.only_cities
    print db.only_cities.find_one()
    return db

def add_country(db):
    db.ciutats.insert({"name" : "Canada"})

def add_city_coord(db, name, lat, lon):
    db.ciutats.insert({"name":name, "lat":lat, "lon":lon})
    
def add_city_coord_2(db, name, lat, lon):
    db.only_cities.insert({"name":name, "lat":lat, "lon":lon})
    
def add_news(db, diari, data, titol, desc):
    db.noticies.insert({"diari":diari, "data":data, "titol":titol, "descripcio":desc})    
    
def get_country(db):
    return db.ciutats.find_one()

def get_coords_city(db, nom):
    a = db.ciutats.find({"name":{'$regex': nom}})
    #a = db.command("text", "ciutats",search=nom, ,limit=10)
    nom.replace(',','')
    nom.split()
    for city in a:
        print city
    return a

def get_aprox_city(db, nom):
    name_search = nom.replace(',','')
    name_search = name_search.split()

def get_examples(db):
    
    a = db.only_cities.find_one({"name": {'$regex':"Barcelona"}})
    b = db.only_cities.find_one({"name": {'$regex':"Girona"}})
    c = db.only_cities.find_one({"name": {'$regex':"Igualada"}})
    d = db.only_cities.find_one({"name": {'$regex':"Terrassa"}})
    e = db.only_cities.find_one({"name": {'$regex':"Manresa"}})
    f = db.only_cities.find_one({"name": {'$regex':"Panadella"}})
    for city in [a,b,c,d,e,f]:
        print city
    return a
    

if __name__ == "__main__":

    db = get_db() 
    add_country(db)
    print get_country(db)