# WEEK 06 - CSV

import csv

with open('data.csv') as file:
    csvReader = csv.reader(file)
    headings = next(csvReader)
    for row in csvReader:
        print(row)