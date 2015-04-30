'''
Created on 14/03/2015

@author: aleix
'''
import json
from SPARQLWrapper import SPARQLWrapper, JSON
 
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)
 
sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX yago: <http://dbpedia.org/class/yago/>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
 
SELECT ?title ?geolat ?geolong
    WHERE {
        #?place rdf:type <http://dbpedia.org/ontology/Place> .
        #?place dbpedia-owl:country <http://dbpedia.org/resource/Spain> .
        ?place foaf:name ?title .
        ?place geo:lat ?geolat .
        ?place geo:long ?geolong .
        FILTER ((?geolong > 0.5 && ?geolong < 2.7) && (?geolat < 42.5 && ?geolat > 40.5)) 
    }
"""
#SELECT count(*)
#    WHERE {
#        ?place rdf:type <http://dbpedia.org/ontology/Place> .
#        ?place foaf:name ?title .
#        ?place geo:lat ?geolat .
#        ?place geo:long ?geolong .
#        FILTER ((?geolong > 0.5 && ?geolong < 2.6) && (?geolat < 42.5 && ?geolat > 40.5))
#    }
)
 
results = sparql.query().convert()
print "Creant Fitxer..."
# Open a file for writing
out_file = open("/home/aleix/ciutats_filtre.json","w")

# Save the dictionary into this file
# (the 'indent=4' is optional, but makes it more readable)
json.dump(results,out_file, indent=4)                                    

# Close the file
out_file.close()

print "Fitxer Creat!"
