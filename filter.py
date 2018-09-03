import csv
 
with open('/media/aditya/Windows/Users/shant/Pictures/data/Data_Entry_2017.csv', 'rt') as inp, open('4177_single_diseases.csv', 'at') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[1].find("00001336_000.png") != -1:
        	print(row[1])
        	writer.writerow(row)
        	break