import xlrd
from collections import OrderedDict
import simplejson as json
import utm
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('CartoCat.xlsx')
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
cars_list = []

print "Conversio iniciada"

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['nom'] = row_values[0]
    cars['tipus'] = row_values[1]
    cars['municipi'] = row_values[2]
    cars['comarca'] = row_values[6]
    cars['utmX'] = row_values[15]
    cars['utmY'] = row_values[16]
    if cars['utmX']==0.0 or cars['utmY']==0.0:
        continue
    u = utm.to_latlon(cars['utmX'],cars['utmY'], 31, 'T')
    cars['lat'] = u[0]
    cars['lon'] = u[1]
    
    cars_list.append(cars)
 
# Serialize the list of dicts to JSON
j = json.dumps(cars_list)
 
# Write to file
with open('CartoCat_Aleix.json', 'w') as f:
    f.write(j)
    
print "Proces acabat"