
import rdflib

g = rdflib.Graph()

# ... add some triples to g somehow ...
g.parse("geo_coordinates_ca_test.ttl", format="nt")

print len(g)
resource = "http://ca.dbpedia.org/resource/"
#s = g.serialize(format='n3')
array = []
primer = True
for s,p,o in g:
    s.replace(resource, "")
    s.replace("_"," ")
    pa=p.split("#")
    print s,p,o
    array.append([s,pa,o])
print "End"

thefile=open("outputDump.txt","w")
for item in array:
    thefile.write("%s\n" % item)