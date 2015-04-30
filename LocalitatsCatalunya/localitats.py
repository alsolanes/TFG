import csv

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'ISO-8859-1') for cell in row]

filename = 'CartoCat.csv'
reader = unicode_csv_reader(open(filename))
for i in xrange(0,10):
    print reader.next()
print reader.next()