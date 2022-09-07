import csv
import json

with open('data/persona.csv','r',newline='',encoding='utf8') as inf, \
     open('data/persona_2.csv','w',newline='',encoding='utf8') as outf:

    r = csv.reader(inf,delimiter='|')
    w = csv.writer(outf,delimiter='|')

    header = next(r)
    w.writerow(header)

    for col1,col2 in r:
        newcol = json.loads(col2)    # Converts JSON to a list
        w.writerow([col1,newcol[0]])