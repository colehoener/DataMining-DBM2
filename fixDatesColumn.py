import csv
import re

with open('cleaned_data.csv', 'r') as fin, open("out.csv",'w') as fout:
        writer = csv.writer(fout)
        for row in csv.reader(fin):
            row[1] = re.sub(r'-1,', '-10,',row[1])
            writer.writerow(row)

