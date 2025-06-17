import csv
import pprint

filename_61 = 'data/61 trader search results.csv'
filename_62 = 'data/62 trader search results.csv'

filename_list = [filename_61, filename_62]

data = []
for filename in filename_list:
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for trader in reader:
            data.append(trader)

pprint.pprint(data)