import csv
 
with open('4999_images.csv', 'rt') as inp, open('4999_images_edit.csv', 'wt') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[1].find("|") == -1:
        	print(row[1])
        	writer.writerow(row)