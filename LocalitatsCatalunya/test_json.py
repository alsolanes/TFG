import json
from pprint import pprint

with open('CartoCat_Aleix.json') as data_file:    
    data = json.load(data_file)

pprint(data)