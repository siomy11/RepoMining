//Read File 'Hello World' Test on Python
import csv
with open('test.csv', 'rb') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    for row in dataReader:
        print(row)
