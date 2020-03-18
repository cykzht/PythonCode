import csv
csvFile = open("fensi.csv", "r")
reader = csv.reader(csvFile)
a = list(reader)
print(a)
for i in a:
    print(i)
