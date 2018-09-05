import csv
 
with open('/media/aditya/Windows/Users/shant/Pictures/data/Data_Entry_2017.csv', 'rt') as inp, open('/media/aditya/Windows/Users/shant/Pictures/data/f25.csv', 'wt') as out:
    writer = csv.writer(out)
    c=0;
    for row in csv.reader(inp):
    	if(c<=25000):
        	if row[1].find("|") == -1:
        		# print(row[1])
        		print (c);
        		writer.writerow(row)
        	# break
        	c=c+1