import sys
import os
import csv

with open('DB_extract.csv', 'r', encoding="utf-8") as input:
    csv_reader = csv.reader(input, delimiter =',')
    linecount = 0
    for row in csv_reader:
        if linecount == 0:
            firstline = row
            linecount +=1
        else:
            cmd = "python3 rainbow.py %s %s %s %s" %(row[0], row[1], row[2], row[3])
            #print(cmd)
            linecount += 1
            os.system(cmd)